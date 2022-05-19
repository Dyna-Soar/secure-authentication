from hashlib import sha256


def hash_password(password):
    encoded_password = bytes(str(password), encoding='utf-8')
    hashed_password = sha256(encoded_password).hexdigest().encode('utf-8')
    return str(hashed_password)


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
    special_chars = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
    for i in range(len(password)):
        if password[i] in special_chars:
            break
        if i == len(password) - 1:
            return False
    return hash_password(password)


def check_hash(password, hash_sent):
    # If hashed password equals hash stored then this is the right password and return true
    if hash_sent == hash_password(password):
        return True
    return False
