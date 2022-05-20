from flask import Flask, request, jsonify

from hashing import create_hashed_password, check_hash

app = Flask(__name__)


@app.route("/request_authentication", methods=['POST'])
def request_authentication():
    if request.form.get("password") is None:
        return jsonify({"Missing Data": "No password provided"}), 400
    if request.form.get("hash_sent") is None:
        return jsonify({"Missing Data": "No hash provided"}), 400
    password = request.form["password"]
    hash_sent = request.form["hash_sent"]
    if check_hash(password, hash_sent):
        return jsonify({"IsPassword": True}), 200
    return jsonify({"IsPassword": False}), 200


@app.route("/hash_new_password", methods=['POST'])
def hash_new_password():
    if request.form.get("password") is None:
        return jsonify({"Missing Data": "No password provided"}), 400
    password = request.form["password"]
    hashed_password = create_hashed_password(password)
    if hashed_password is False:
        return jsonify({"Error Message": "Password not valid, should contain at least 8 characters; 1 digit; 1 special character"}), 406
    return jsonify({"hashed_password": hashed_password}), 200
