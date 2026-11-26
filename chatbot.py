"""Rule-based financial chatbot prototype. Run: python chatbot.py"""
import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "financial_data.csv"

QUERIES = [
    "What is the total revenue?",
    "How has net income changed over the last year?",
    "What are the total assets and liabilities?",
    "What is the cash flow from operating activities?",
    "What is the net profit margin?",
]


def load_data(path=DATA_FILE):
    """Return {company: [yearly rows, oldest first]}. Amounts are in USD millions."""
    data = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            company = row.pop("company")
            data.setdefault(company, []).append({k: int(v) for k, v in row.items()})
    for rows in data.values():
        rows.sort(key=lambda r: r["fiscal_year"])
    return data


DATA = load_data()


def normalize(text):
    """Ignore capital letters, extra spaces and ending punctuation."""
    return " ".join(text.lower().split()).rstrip("?.! ")


def money(millions):
    sign = "-" if millions < 0 else ""
    return f"{sign}${abs(millions):,} million"


def change(new, old):
    """Describe the movement from old to new."""
    diff = new - old
    if diff == 0:
        return "was unchanged"
    word = "increased" if diff > 0 else "decreased"
    percent = f" ({abs(diff) / abs(old):.1%})" if old else ""
    return f"{word} by {money(abs(diff))}{percent}"


def simple_chatbot(user_query, company):
    """Match a predefined query and answer it for the chosen company."""
    query = normalize(user_query)
    previous, latest = DATA[company][-2], DATA[company][-1]
    year, prior_year = latest["fiscal_year"], previous["fiscal_year"]

    if query == normalize(QUERIES[0]):
        return (f"{company}'s total revenue in FY{year} was {money(latest['total_revenue'])}. "
                f"It {change(latest['total_revenue'], previous['total_revenue'])} from FY{prior_year}.")
    elif query == normalize(QUERIES[1]):
        return (f"{company}'s net income {change(latest['net_income'], previous['net_income'])}, "
                f"from {money(previous['net_income'])} in FY{prior_year} "
                f"to {money(latest['net_income'])} in FY{year}.")
    elif query == normalize(QUERIES[2]):
        return (f"At the end of FY{year}, {company} had total assets of {money(latest['total_assets'])} "
                f"and total liabilities of {money(latest['total_liabilities'])}.")
    elif query == normalize(QUERIES[3]):
        return (f"{company}'s operating cash flow in FY{year} was {money(latest['operating_cash_flow'])}. "
                f"It {change(latest['operating_cash_flow'], previous['operating_cash_flow'])} "
                f"from FY{prior_year}.")
    elif query == normalize(QUERIES[4]):
        now = latest["net_income"] / latest["total_revenue"]
        before = previous["net_income"] / previous["total_revenue"]
        return (f"{company}'s net profit margin was {now:.1%} in FY{year}, "
                f"compared with {before:.1%} in FY{prior_year}.")
    else:
        return "Sorry, I can only provide information on predefined queries. Type 'help' to see them."


def find_company(text):
    return next((name for name in DATA if name.lower() == normalize(text)), None)


def help_text():
    lines = [f"  {i}. {q}" for i, q in enumerate(QUERIES, 1)]
    return ("Questions (type the number or the full question):\n" + "\n".join(lines)
            + f"\nType a company name to switch ({', '.join(DATA)}), 'help' or 'exit'.")


def respond(user_input, company):
    """Handle one line of input. Return (reply, selected company)."""
    text = normalize(user_input)
    new_company = find_company(text)
    if new_company:
        return f"Company set to {new_company}.", new_company
    if text == "help":
        return help_text(), company
    if text.isdecimal() and 1 <= int(text) <= len(QUERIES):
        user_input = QUERIES[int(text) - 1]
    if company is None:
        return f"Please choose a company first: {', '.join(DATA)}.", company
    return simple_chatbot(user_input, company), company


def main():
    company = None
    print("Financial Chatbot Prototype\n" + help_text())
    while True:
        try:
            user_input = input(f"\n[{company or 'no company'}] You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if normalize(user_input) in ("exit", "quit"):
            break
        reply, company = respond(user_input, company)
        print("Bot:", reply)
    print("Bot: Goodbye!")


if __name__ == "__main__":
    main()
