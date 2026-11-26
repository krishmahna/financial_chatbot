"""Run: python test_chatbot.py  (rewrites test_results.txt)"""
from pathlib import Path
from chatbot import DATA, QUERIES, respond

results, passed, total = [], 0, 0


def check(label, user_input, company, expected):
    global passed, total
    reply, selected = respond(user_input, company)
    ok = expected in reply
    total += 1
    passed += ok
    results.append(f"[{'PASS' if ok else 'FAIL'}] {label}\n  Input: {user_input!r} (company: {company})\n  Reply: {reply}\n")
    return selected


# Every predefined query for every company: the reply must name the company and latest year
for name, rows in DATA.items():
    for q in QUERIES:
        reply, _ = respond(q, name)
        check(f"{name}: {q}", q, name, f"FY{rows[-1]['fiscal_year']}")

# Expected values worked out separately from the source figures
check("Revenue value", QUERIES[0], "Microsoft", "$331,839 million")
check("Net income rise", QUERIES[1], "Apple", "increased by $20,165 million (18.0%)")
check("Net income fall", QUERIES[1], "Tesla", "decreased by $3,297 million (46.5%)")
check("Assets and liabilities", QUERIES[2], "Apple", "$292,455 million")
check("Cash flow value", QUERIES[3], "Tesla", "$14,747 million")
check("Profit margin", QUERIES[4], "Microsoft", "40.3%")
# Input handling
check("Case and spacing", "  what is the TOTAL revenue  ", "Apple", "$478,834 million")
check("Number shortcut", "1", "Tesla", "$94,827 million")
check("Company switch", "tesla", "Apple", "Company set to Tesla")
check("No company yet", "1", None, "choose a company")
check("Help", "help", None, "Questions")
check("Unknown query", "What is the stock price?", "Apple", "only provide information")
check("Out-of-range number", "9", "Apple", "only provide information")
check("Empty input", "", "Apple", "only provide information")

summary = f"{passed}/{total} tests passed"
Path(__file__).with_name("test_results.txt").write_text(summary + "\n\n" + "\n".join(results), encoding="utf-8")
print(summary)
raise SystemExit(passed != total)
