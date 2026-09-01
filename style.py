import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@600;700&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Source Serif 4', Georgia, serif !important;
        color: #161B22 !important;
        letter-spacing: -0.01em;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header [data-testid="stToolbar"] {visibility: hidden;}

    [data-testid="stSidebar"] {
        background-color: #161B22;
    }
    [data-testid="stSidebar"] * {
        color: #E7E2D6 !important;
    }
    [data-testid="stSidebar"] a {
        border-radius: 6px;
    }

    .stButton>button {
        background-color: #B08A3E;
        color: #161B22;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        padding: 0.5rem 1.3rem;
        transition: background-color 0.15s ease;
    }
    .stButton>button:hover {
        background-color: #C7A050;
        color: #161B22;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 10px !important;
        border: 1px solid #E4DFD3 !important;
        box-shadow: 0 1px 3px rgba(22,27,34,0.06);
    }

    [data-testid="stTextInput"] input, textarea {
        border-radius: 6px !important;
        border: 1px solid #D9D2C0 !important;
    }
    </style>
    """, unsafe_allow_html=True)