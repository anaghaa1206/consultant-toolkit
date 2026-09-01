import streamlit as st
from style import inject_custom_css
inject_custom_css()
from agent_core import get_client, run_agent
from auth import check_access

st.title("✉️ Client Status Update Drafter")
st.write("Give it a few bullet points on project progress, and get a polished client-ready email.")

api_key = check_access()

bullets = st.text_area(
    "Progress bullet points",
    placeholder="e.g. Finished data migration for phase 1. Testing starts next week. One vendor delay pushed go-live by 3 days.",
    height=140
)

tone = st.selectbox("Tone", ["Professional and warm", "Formal", "Brief and direct"])

SYSTEM_PROMPT = f"""You draft client status update emails from bullet points.
Tone: {tone}.
Once you have a complete draft, call the format_email tool exactly once with the
finished subject line and body. Do not call it more than once."""

tools = [
    {
        "name": "format_email",
        "description": "Submits the finished drafted email as a separate subject and body.",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["subject", "body"]
        }
    }
]

if st.button("Draft Email", type="primary"):
    if not api_key:
        st.error("Please enter your API key above first.")
    elif not bullets:
        st.error("Please add a few progress bullet points first.")
    else:
        with st.spinner("Drafting..."):
            client = get_client(api_key)
            _, drafts = run_agent(client, SYSTEM_PROMPT, tools, bullets, collect_tool_calls=True)
        if drafts:
            email = drafts[0]
            st.text_input("Subject", value=email["subject"])
            st.text_area("Body", value=email["body"], height=250)
        else:
            st.info("No draft was produced — try adding more detail to your bullet points.")