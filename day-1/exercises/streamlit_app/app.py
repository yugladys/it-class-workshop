import streamlit as st
import pandas as pd

st.title("Welcome to the Streamlit App")
st.write("This is a simple streamlit application")

st.header("Information")
st.write("The current technical workshop is delivered on Docker and Kubernetes")

data = pd.read_csv('data.csv')

st.header("Level of participants in the workshop")
st.write(data)