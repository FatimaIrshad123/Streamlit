import streamlit as st
import hashlib
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

stored_data = {
    "user1_data": {"encrypted_text": "some_ciphertext", "passkey": "hashed_passkey"},
}
failed_attempts = 0

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


def encrypt(text, passkey):
    encryted =  cipher.encrypt(text.encode()).decode()
    return encryted

def decrypt(encypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    global failed_attempts
    print('hashed_passkey',hashed_passkey)

    for key, value in stored_data.items():
        if (value["encrypted_text"] == encypted_text) and (value["passkey"] == hashed_passkey):
            decrypted = cipher.decrypt(encypted_text.encode()).decode()
            failed_attempts = 0
            return decrypted
    failed_attempts += 1
    print(f"Failed attempts: {failed_attempts}")
    return None

print(decrypt('some_ciphertext', "hashed_passkey"))

st.title("Encryption and Decryption App")
st.write("This app allows you to encrypt and decrypt text using a passkey.")