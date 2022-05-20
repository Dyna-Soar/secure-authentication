import pytest


class TestRequestAuthentication:
    def test_request_invalid_authentication(self, fixture_client, fixture_users_passwords):
        response = fixture_client.post("/request_authentication", data={
            'password': fixture_users_passwords[1]["password"],
            'hash_sent': fixture_users_passwords[1]["hashed_password"]
        })
        assert response.status_code == 200
        assert b'false' in response.data

    def test_request_valid_authentication(self, fixture_client, fixture_users_passwords):
        response = fixture_client.post("/request_authentication", data={
            'password': fixture_users_passwords[0]["password"],
            'hash_sent': fixture_users_passwords[0]["hashed_password"]
        })
        assert response.status_code == 200
        assert b'true' in response.data

    def test_no_password_authentication(self, fixture_client, fixture_users_passwords):
        response = fixture_client.post("/request_authentication", data={
            'hash_sent': fixture_users_passwords[0]["hashed_password"]
        })
        assert response.status_code == 400
        assert b'Missing Data' in response.data

    def test_no_hash_authentication(self, fixture_client, fixture_users_passwords):
        response = fixture_client.post("/request_authentication", data={
            'password': fixture_users_passwords[0]["password"],
        })
        assert response.status_code == 400
        assert b'Missing Data' in response.data


class TestRequestNewHash:
    def test_password_less8char(self, fixture_client):
        response = fixture_client.post("/hash_new_password", data={'password': "ascz"})
        assert response.status_code == 406

    def test_password_nodigit(self, fixture_client):
        response = fixture_client.post("/hash_new_password", data={'password': "asczhiflx"})
        assert response.status_code == 406

    def test_password_nospechar(self, fixture_client):
        response = fixture_client.post("/hash_new_password", data={'password': "asczhiflx8"})
        assert response.status_code == 406

    def test_password_valid(self, fixture_client):
        response = fixture_client.post("/hash_new_password", data={'password': "asczhiflx.8"})
        assert response.status_code == 200
        assert b'hashed_password' in response.data

    def test_no_password(self, fixture_client):
        response = fixture_client.post("/hash_new_password")
        assert response.status_code == 400
        assert b'Missing Data' in response.data
