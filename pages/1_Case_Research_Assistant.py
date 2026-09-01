import streamlit as st
from style import inject_custom_css
inject_custom_css()
from agent_core import get_client, run_agent
from auth import check_access

st.title("📊 Case Research Assistant")
st.write("Describe a business/technology investment scenario, and get a structured case analysis.")

api_key = check_access()

scenario = st.text_area(
    "Scenario",
    placeholder="e.g. A hospital network is considering wearable patient monitoring costing $480,000 upfront, saving $290,000/year in avoided readmission penalties. Should they proceed?",
    height=120
)

SYSTEM_PROMPT = """You are a case research assistant for a technology consulting analyst.
Given a business scenario, structure it the way a consultant would:
1. Write a Situation-Complication-Question (SCQ) framing.
2. Break the question into a 4-branch issue tree: technical feasibility, financial case,
   implementation risk, organizational readiness.
3. Use the calculate_payback tool whenever cost and benefit figures are given — never do
   this math yourself, always call the tool.
4. End with an answer-first recommendation: state it first, then three supporting reasons,
   then the biggest risk and a mitigation.
Be concise and structured. Use headers."""

tools = [
    {
        "name": "calculate_payback",
        "description": "Calculates the payback period in months for a business investment, given the upfront cost and expected annual financial benefit.",
        "input_schema": {
            "type": "object",
            "properties": {
                "upfront_cost": {"type": "number"},
                "annual_benefit": {"type": "number"}
            },
            "required": ["upfront_cost", "annual_benefit"]
        }
    }
]

if st.button("Run Analysis", type="primary"):
    if not api_key:
        st.error("Please enter your API key above first.")
    elif not scenario:
        st.error("Please describe a scenario first.")
    else:
        with st.spinner("Structuring the case..."):
            client = get_client(api_key)
            result = run_agent(client, SYSTEM_PROMPT, tools, scenario)
        st.markdown(result)