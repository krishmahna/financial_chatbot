# Financial Chatbot Prototype

Built with AI assistance.

## How it works
`chatbot.py` loads `financial_data.csv`, asks you to choose a company, and matches your
question to one of five predefined queries using if/elif statements. Matching ignores
capital letters, extra spaces and ending punctuation. Changes and margins are calculated
from the data, so the numbers are not typed into the replies.

## Run it (Python 3.8 or later, no extra libraries)
    python chatbot.py         # start the chatbot
    python test_chatbot.py    # run the tests

On some computers the command is `python3` (Mac/Linux) or `py` (Windows).

## Predefined queries
1. What is the total revenue?
2. How has net income changed over the last year?
3. What are the total assets and liabilities?
4. What is the cash flow from operating activities?
5. What is the net profit margin?

Type a number or the full question. Type a company name to switch, `help`, or `exit`.

## Testing
29 of 29 automated tests passed (`test_results.txt`): all 5 queries for all 3 companies
(these check that a reply comes back for the latest year), 6 value checks, and 8 input
handling checks. `sample_session.txt` is a transcript produced by feeding scripted input
to the chatbot.

## Limitations
- No AI or language understanding: reworded or misspelled questions are rejected.
- Covers only Microsoft, Apple and Tesla, and five questions.
- Data is stored in a CSV file and does not update by itself.
- Replies compare only the latest two years. The earliest year is stored but not shown.
- Fiscal years differ: Microsoft ends in June, Apple in September, Tesla in December.
  Compare companies with care.
- Tesla net income is the amount attributable to common stockholders.
- No memory beyond the selected company. Command line only.
- Not investment advice.

## Data (USD millions, collected 27 November 2026)
This data was gathered from public sources for this prototype; it is not a copy of an
earlier Task 1 analysis. Some figures come from third-party summaries of company filings.
Check them against your Task 1 data and the original filings before relying on them.

- Microsoft annual report 2026: https://www.microsoft.com/investor/reports/ar26/index.html
- Microsoft multi-year figures: https://stockfactsheet.com/stocks/msft/financials/
- Microsoft 2024 operating cash flow: https://open10k.com/MSFT
- Apple FY2026 and FY2025: https://www.apple.com/newsroom/pdfs/fy2026q4/FY26_Q4_Consolidated_Financial_Statements.pdf
- Apple FY2024: https://images.apple.com/newsroom/pdfs/fy2024-q4/FY24_Q4_Consolidated_Financial_Statements.pdf
- Tesla 2025: https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf
- Tesla 2024 and 2023 balance sheets: https://ir.tesla.com/_flysystem/s3/sec/000162828025003063/tsla-20241231-gen.pdf
- Tesla liabilities and multi-year figures: https://app.dhicapitalgroup.com/research/TSLA , https://analytics.stackrader.com/company/TSLA
- Tesla 2023 revenue and net income: https://bullfincher.io/companies/tesla/financial-statements , https://www.moomoo.com/news/notice/151327584/tesla-10-k-annual-report
