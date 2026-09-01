import streamlit as st
from style import inject_custom_css
inject_custom_css()
import pandas as pd
from agent_core import get_client, run_agent
from auth import check_access

st.title("📝 Meeting Notes → Action Items")
st.write("Paste messy meeting notes below, and get a clean, structured action item list.")

api_key = check_access()

notes = st.text_area(
    "Meeting notes",
    placeholder="e.g. Sarah will follow up with the client on the SOW by Friday. Need to check with legal about the data clause before next Tuesday's call, that's on Raj...",
    height=180
)

SYSTEM_PROMPT = """You extract action items from messy meeting notes.
For every distinct task you find, call the log_action_item tool once, with:
- task: a short, clear description of what needs to be done
- owner: who is responsible (use "Unassigned" if not stated)
- deadline: when it's due (use "Not specified" if not stated)
After logging all action items, write one short confirmation sentence."""

tools = [
    {
        "name": "log_action_item",
        "description": "Logs a single action item extracted from meeting notes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string"},
                "owner": {"type": "string"},
                "deadline": {"type": "string"}
            },
            "required": ["task", "owner", "deadline"]
        }
    }
]

if st.button("Extract Action Items", type="primary"):
    if not api_key:
        st.error("Please enter your API key above first.")
    elif not notes:
        st.error("Please paste some meeting notes first.")
    else:
        with st.spinner("Reading through the notes..."):
            client = get_client(api_key)
            summary, action_items = run_agent(client, SYSTEM_PROMPT, tools, notes, collect_tool_calls=True)
        st.markdown(summary)
        if action_items:
            st.subheader("Action Items")
            df = pd.DataFrame(action_items)
            st.table(df)
        else:
            st.info("No clear action items were found in these notes.")