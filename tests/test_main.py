import pytest

from main import app

client = app.test_client()


class TestRequestAuthentication:
    def test_request_authentication(self):
        pass


class TestRequestNewHash:
    def test_password_less8char(self):
        response = client.post("/hash_new_password", data={'password': "ascz"})
        assert response.status_code == 406

    def test_password_nodigit(self):
        response = client.post("/hash_new_password", data={'password': "asczhiflx"})
        assert response.status_code == 406

    def test_password_nospechar(self):
        response = client.post("/hash_new_password", data={'password': "asczhiflx8"})
        assert response.status_code == 406

    def test_password_valid(self):
        response = client.post("/hash_new_password", data={'password': "asczhiflx.8"})
        assert response.status_code == 200
        assert "hashed_password" in response.data
