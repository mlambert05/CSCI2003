import streamlit as st
import pandas as pd
import mysql.connector



st.title("Hello, Streamlit!")
st.write("this is my first streamlit app")

import streamlit as st

st.title("Interactive Streamlit App")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")

