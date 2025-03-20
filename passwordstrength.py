import re
import streamlit as st

st.set_page_config(
    page_title="🔐Password Strength Meter",
    page_icon="🧊",
    
    initial_sidebar_state="expanded"
)

def check_password_strength(password):
    
    if not password:
        st.warning("Enter password to check strength")
        return

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.write("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*/]", password):
        score += 1
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
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
# Get user input
st.title("🔐 Password Strength Meter")
#st.slider.title("Password Strength Checker")
password = st.text_input("Enter your password here", type="password")

if st.button("Check Strength"):
    check_password_strength(password)