import streamlit as st
import hashlib
from cryptography.fernet import Fernet

key = b'VCJQDxVYatd_SlwYuACAsfFDFq3hm2TzZDXCt_B8s1I=' #Fernet.generate_key()
cipher = Fernet(key)

stored_data = {}
failed_attempts = 0

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


def encrypt(text, passkey):
    encrypted =  cipher.encrypt(text.encode()).decode()
    return encrypted

def decrypt(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    global failed_attempts
    print('hashed_passkey',hashed_passkey)

    for key, value in stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            try:
                decrypted = cipher.decrypt(encrypted_text.encode()).decode()
                print('decrypted',decrypted)
                failed_attempts = 0
                return decrypted
            except Exception as e:
                st.error(f"Decryption error: {e}")

    failed_attempts += 1
    print(f"Failed attempts: {failed_attempts}")
    return None


menu = ["🏠 Home","📂 Store Data","🔍 Retrieve Data","🛡️ Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "🏠 Home":
    st.title("🏠 Welcome to the Secure Data Encryption System")

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

elif choice == "📂 Store Data":
    st.title("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt(user_data, passkey)
            stored_data["user1"] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            print('stored_data',stored_data)
            st.success("✅ Data stored securely!")
            st.write(f"Encrypted Text: {encrypted_text}")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "🔍 Retrieve Data":
    st.title("🔍 Retrieve Data")
    encrypted_text = st.text_input("Enter Encrypted text:")
    passkey = st.text_input("Enter passkey:", type="password")
    print('encrypted_text',encrypted_text)

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt(encrypted_text, passkey)
            
            if decrypted_text:
                st.success(f"✅ Decrypted Text: {decrypted_text}")
            else:
                st.error("❌ Decryption failed. Please check your inputs.")

                if failed_attempts >= 3:
                    st.warning("🔒 You have made too many failed attempts. Please try again later.")
        else:
            st.error("⚠️ Please enter both encrypted text and passkey.")

elif choice == "🛡️ Login":
    st.title("🔑 Authorization Required")
    
    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("Enter Username:")

    with col2:
        login_pass = st.text_input("Enter Password:", type="password")

    if st.button("Login"):
        if username == "fatima" and login_pass == "admin":  # Hardcoded for demo, replace with proper auth
            st.success("✅ Login successful!")
        else:
            st.error("❌ Incorrect password!")

st.markdown("---")
st.markdown("Made by Fatima Irshad | 🔗 [GitHub](https://github.com/FatimaIrshad123) | 🔗 [Linkedin](https://www.linkedin.com/in/fatima-irshad-97a5a92a7/)")