from hashlib import sha256


def hash_password(password):
    hashed_password = sha256(password).hexdigest()
    return hashed_password


def create_hashed_password(password):
    # Check for 8 characters minimum and 128 max
    if len(password) < 8 or len(password) > 128:
        return False
    # Check for 1 number
    for i in range(len(password)):
        if password[i].isdigit():
            break
        if i == len(password) - 1:
            return False
    # Check for 1 special character
    for i in range(len(password)):
        if not password[i].alphanum():
            break
        if i == len(password) - 1:
            return False


def check_hash(password, hash_sent):
    # If hashed password equals hash stored then this is the right password and return true
    if hash_sent == hash_password(password):
        return True
    return False