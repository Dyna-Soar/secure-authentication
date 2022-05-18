from flask import Flask

from json import dumps

from hashing import create_hashed_password, check_hash

app = Flask(__name__)


@app.route("/request_authentication", methods=['POST'])
def request_authentication(password, hash_sent):
    if check_hash(password, hash_sent):
        return dumps({"IsPassword": True}), 200
    return dumps({"IsPassword": False}), 200


@app.route("/hash_new_password", methods=['POST'])
def hash_new_password(password):
    hashed_password = create_hashed_password(password)
    if hashed_password is False:
        return dumps({"Message": "Password has to contain at least 8 characters; 1 digit; 1 special character"}), 202
    return dumps({"hashed_password": hashed_password}), 200
