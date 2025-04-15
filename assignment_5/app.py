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

st.title("🏠 Welcome to the Secure Data Encryption System")

menu = ["Home","Insert Data","Retrieve Data","Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.markdown("### 🔐 Secure, Simple & Smart")
    st.markdown("""
    Welcome to your personal data vault!  
    This app allows you to securely **encrypt, store, and retrieve sensitive data** with passkey protection.  
    """)

    st.markdown("#### 🌟 Features:")
    st.markdown("""
    - 🔒 **Encrypt** your private messages with a secure key  
    - 🔑 **Password-protected access** to sensitive information  
    - 🧠 Easy-to-use interface with clear instructions  
    - 📥 **Retrieve** your data safely anytime  
    - 🚫 Lockout after 3 failed login attempts
    """)

    st.info("Use the sidebar to navigate through the app.")

elif choice == "Insert Data":
    st.subheader("Insert Data")
    text = st.text_area("Enter text to encrypt:")
    passkey = st.text_input("Enter passkey:", type="password")

    if st.button("Encrypt"):
        if text and passkey:
            encrypted_text = encrypt(text, passkey)
            st.success(f"Encrypted Text: {encrypted_text}")
        else:
            st.error("Please enter both text and passkey.")

elif choice == "Retrieve Data":
    st.subheader("Retrieve Data")
    encrypted_text = st.text_input("Enter encrypted text:")
    passkey = st.text_input("Enter passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt(encrypted_text, passkey)
            if decrypted_text:
                st.success(f"Decrypted Text: {decrypted_text}")
            else:
                st.error("Decryption failed. Please check your inputs.")
        else:
            st.error("Please enter both encrypted text and passkey.")

elif choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
            st.warning("You have made too many failed attempts. Please try again later.")


st.markdown("---")
st.markdown("Made with ❤️ by Fatima | 🔗 [GitHub](https://github.com/FatimaIrshad123)")