# Secure-Authentication API

This is an API for creating hashed passwords and authenticate users. The API rely of on sha256 hashing functions and Flask for endpoints


### How to run the application
1. Run `export FLASK_APP=main.py`
2. ERun `flask run`

### Endpoints
- Check authentication at `/request_authentication` endpoint, which takes password as first argument and hashed_password as second argument

- Create hashed password at `/hash_new_password` endpoint, which takes password as argument

### Testing
To test endpoints run: `python -m pytest tests/ -v`