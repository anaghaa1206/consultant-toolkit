import streamlit as st
from style import inject_custom_css

st.set_page_config(page_title="Consultant Toolkit", page_icon="🧰", layout="wide")
inject_custom_css()

st.title("Consultant Toolkit")
st.markdown(
    "<p style='color:#3D4A5C; font-size:16px; max-width:600px;'>"
    "Three small agents for the repetitive parts of consulting work — "
    "case research, meeting follow-through, and client communication.</p>",
    unsafe_allow_html=True
)

st.write("")
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("📊 **Case Research Assistant**")
        st.caption("Structures a business case with financial modeling and a recommendation.")
        st.page_link("pages/1_Case_Research_Assistant.py", label="Open tool →")

with col2:
    with st.container(border=True):
        st.markdown("📝 **Meeting Notes → Action Items**")
        st.caption("Turns messy meeting notes into a clean, structured task list.")
        st.page_link("pages/2_Meeting_Notes.py", label="Open tool →")

with col3:
    with st.container(border=True):
        st.markdown("✉️ **Client Status Drafter**")
        st.caption("Turns bullet points into a polished, client-ready email.")
        st.page_link("pages/3_Client_Status_Drafter.py", label="Open tool →")

st.write("")
st.divider()
st.caption("Built with the Claude API to explore agentic tool use in everyday consulting workflows.")