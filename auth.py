import streamlit as st

def check_access():
    """Gates a page behind a shared access code, and returns the server-side API key."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.subheader("🔒 Access required")
        st.caption("This demo is access-gated to protect API usage. Ask for the code.")
        code = st.text_input("Access code", type="password")
        if st.button("Enter"):
            if code == st.secrets.get("APP_PASSWORD", ""):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect access code.")
        st.stop()

    return st.secrets["ANTHROPIC_API_KEY"]
