import json

# --- Case Research Assistant tools ---

def calculate_payback(upfront_cost: float, annual_benefit: float) -> dict:
    """Calculates payback period in months given an upfront cost and annual benefit."""
    if annual_benefit <= 0:
        return {"error": "Annual benefit must be greater than zero."}
    payback_years = upfront_cost / annual_benefit
    payback_months = round(payback_years * 12, 1)
    return {
        "upfront_cost": upfront_cost,
        "annual_benefit": annual_benefit,
        "payback_period_months": payback_months
    }

def save_section(section_title: str, content: str, filename: str = "case_output.md") -> dict:
    """Appends a titled section to a markdown output file."""
    with open(filename, "a") as f:
        f.write(f"\n## {section_title}\n\n{content}\n")
    return {"status": "saved", "section": section_title, "file": filename}

# --- Meeting Notes agent tool ---

def log_action_item(task: str, owner: str, deadline: str) -> dict:
    """Logs a single action item. Returns it so the app can collect a running list."""
    return {"task": task, "owner": owner, "deadline": deadline}

# --- Client Status Drafter tool ---

def format_email(subject: str, body: str) -> dict:
    """Structures a drafted email into separate subject and body fields."""
    return {"subject": subject, "body": body}