import streamlit as st
import pandas as pd
import os
from io import BytesIO
import numpy as np

st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter")
st.write("Convert your units easily!")


option1 = st.selectbox(
    "Please Select Unit?",
    ("centimeter", "meter", "gram", "kilogram"),
)

select1 = st.write("You selected:", option1)

option2 = st.selectbox(
    "Please Select Unit to which you want to convert?",
    ("centimeter", "meter", "gram", "kilogram"),
)

select2 = st.write("You selected:", option2)

number = st.number_input("Enter Number to Convert")

if st.button("Convert"):
    if option1=="centimeter" and option2=="meter":
        meters_value = number / 100  # Conversion logic
        st.success(f"**Length in meters:** {meters_value} m")

    elif option1=="meter" and option2=="centimeter":
        centimeters_value = number * 100  # Conversion logic
        st.success(f"**Length in centimeter:** {centimeters_value} cm")

    elif option1=="gram" and option2=="kilogram":
        kilogram_value = number / 1000  # Conversion logic
        st.success(f"**Weight in kilogram:** {kilogram_value} kg")

    elif option1=="kilogram" and option2=="gram":
        gram_value = number * 1000  # Conversion logic
        st.success(f"**Weight in gram:** {gram_value} g")

    elif option1==option2:
        st.success(f"**The answer in {option2} is:** {number}")

    else: 
        st.error(f"{option1} is not convertable to {option2}")