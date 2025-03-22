import re
import streamlit as st
import string
import secrets
import random

st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔐",    
    initial_sidebar_state="expanded"
)

def check_password_strength(password):
    
    if not password:
        st.warning("Enter password to check strength")
        return

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        st.write("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*/]", password):
        score += 1
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

    if feedback:
        for msg in feedback:
            st.write(msg)
    st.write(f"You scored {score} out of 4")

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password here", type="password")

if st.button("Check Strength"):
    check_password_strength(password)


def generate_password(length):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = '-_!@#$%^&*/'

    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    all_chars = lower + upper + digits + special
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    random.shuffle(password)

    return ''.join(password)

st.title("🔑Need a strong password?")

if st.button("Generate Password"):
    password = generate_password(8)
    st.success(f"Password Generated: {password}")