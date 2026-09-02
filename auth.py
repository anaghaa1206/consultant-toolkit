import streamlit as st

def check_access():
    return st.secrets["ANTHROPIC_API_KEY"]
