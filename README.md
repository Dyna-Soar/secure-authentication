# This is an API for creating hashed passwords and authenticate users

## The API relies of on sha256 hashing functions and Flask for endpoints

### Enter `export FLASK_APP=main.py`
### Enter `flask run`

### Check authentication at `/request_authentication` endpoint, which takes password as first argument and hashed_password as second argument

### Create hashed password at `/hash_new_password` endpoint, which takes password as argument

### To test endpoints run: `python -m pytest tests/ -v`