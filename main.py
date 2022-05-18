from flask import Flask

from hashing import hash_password, create_hashed_password, check_hash

app = Flask(__name__)


@app.route("/request_authentication")
def request_authentication(password, hash_sent):
    if check_hash(password, hash_sent):
        return True
    return False


@app.route("/hash_new_password")
def hash_new_password(password):
    return create_hashed_password(password)
