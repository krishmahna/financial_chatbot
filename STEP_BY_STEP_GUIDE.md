# How to build this chatbot, step by step

## Step 1: Prepare
1. Install Python 3 from python.org. On Windows, tick "Add Python to PATH".
2. Check it in a terminal: `python --version`
3. Create a folder named `financial_chatbot` and open it in an editor such as VS Code.
4. pandas and Flask are not needed: the built-in `csv` module and `input()` are enough.

## Step 2: Prepare the data
1. Review your Task 1 figures.
2. Create `financial_data.csv` with these columns:
   company, fiscal_year, total_revenue, net_income, total_assets,
   total_liabilities, operating_cash_flow
3. Add one row per company per year. Use the same unit (USD millions), no commas in numbers.

## Step 3: Design the queries
Choose 3 to 5 questions (this project uses 5) and decide which columns answer each one.
Net profit margin = net income / total revenue.
Change % = (new - old) / absolute value of old.

## Step 4: Write chatbot.py
Build it in this order:
1. `load_data()`: read the CSV, group rows by company, sort by year.
2. `normalize()`: lower-case the input and remove extra spaces and ending punctuation.
3. `money()` and `change()`: format amounts and describe increases or decreases.
4. `simple_chatbot()`: one if/elif branch per query, plus an else for unknown questions.
5. `respond()`: handle company names, `help` and number shortcuts.
6. `main()`: a `while True` loop that reads with `input()`, prints the reply and stops on `exit`.

Run it after each addition to catch mistakes early.

## Step 5: Try it
    python chatbot.py
Type `apple`, then `1`, then `2`, then `tesla`, then `5`, then `exit`.

## Step 6: Test
Write `test_chatbot.py`. For each case, send an input and check that the reply contains the
expected text. Work out expected values separately, for example Apple's net income change:
132175 - 112010 = 20165. Include bad input too. Run `python test_chatbot.py`.

## Step 7: Document
Write `README.md`: how it works, supported queries, how to run it, limitations, data sources.

## Step 8: Package and submit
Put all files in the folder, then:
- Windows: right-click the folder, choose "Compress to ZIP file"
  (Windows 10: "Send to" > "Compressed (zipped) folder").
- Mac: right-click the folder, choose "Compress".
Unzip a copy and run it once before submitting.

## Optional next steps
Add keyword matching so reworded questions work, or add a Flask web page that calls `respond()`.
