import pytest

from main import app


@pytest.fixture()
def fixture_client():
    client = app.test_client()
    return client

@pytest.fixture()
def fixture_users_passwords():
    users = [
        {"password": "apyng!05.ps", "hashed_password": "b'ae7404c9244015915be965596fce7aeb64750e80b991f202e4e78fbb689e765a'"},
        {"password": "kod(mh4zoj", "hashed_password": "fake_hash"}
    ]
    return users
