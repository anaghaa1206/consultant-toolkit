import anthropic
import json
from tools import calculate_payback, save_section, log_action_item, format_email

def get_client(api_key: str):
    return anthropic.Anthropic(api_key=api_key)

def run_agent(client, system_prompt: str, tools: list, user_input: str, collect_tool_calls: bool = False):
    """
    Runs the tool-use agent loop. If collect_tool_calls=True, also returns a list
    of every tool call made (useful for building structured tables, like action items).
    """
    messages = [{"role": "user", "content": user_input}]
    collected_calls = []

    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1500,
            system=system_prompt,
            tools=tools,
            messages=messages
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    if block.name == "calculate_payback":
                        result = calculate_payback(**block.input)
                    elif block.name == "save_section":
                        result = save_section(**block.input)
                    elif block.name == "log_action_item":
                        result = log_action_item(**block.input)
                        collected_calls.append(result)
                    elif block.name == "format_email":
                        result = format_email(**block.input)
                        collected_calls.append(result)
                    else:
                        result = {"error": "unknown tool"}
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result)
                    })
            messages.append({"role": "user", "content": tool_results})
            continue

        final_text = "".join(block.text for block in response.content if block.type == "text")
        if collect_tool_calls:
            return final_text, collected_calls
        return final_text