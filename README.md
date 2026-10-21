# 🤖 Dynamic AI Text-to-SQL Analytics Assistant

An end-to-end, locally hosted analytics assistant built with Streamlit, Python, and the Google Gemini API. The app translates plain-English business questions into executable SQLite queries, fetches the underlying data, and dynamically routes the presentation layer into natural-language answers, structured data tables, or interactive bar charts based on the analytical intent.

---

## 💡 What It Does

- **Natural Language Querying:** Query tabular business records without writing manual SQL.
- **Dynamic Presentation Engine:** An LLM-driven routing layer classifies queries and renders the output as:
  - **Statements:** Summarized natural sentences for single-metric lookups.
  - **Tables:** Structured tabular grids for entity lists and record lookups.
  - **Bar Charts:** Visual comparative graphs for aggregations across categories.
- **Transparency:** Displays the generated SQL syntax alongside the query results.

---

## 🛠️ Tech Stack

- **Application Framework:** Streamlit
- **LLM Engine:** Google Gemini API (`gemini-3.8-flash`)
- **Database Engine:** SQLite (`company.db`)
- **Data Manipulation:** Pandas
- **Language:** Python 3.10+

---

## 📋 Database Schema

The local database (`company.db`) includes:

- `employees`: `id` (INTEGER), `name` (TEXT), `department` (TEXT), `salary` (INTEGER)
- `sales`: `sale_id` (INTEGER), `employee_id` (INTEGER), `amount` (INTEGER), `month` (TEXT)

---

## 🚀 Quickstart Guide

### 1. Clone the repository
```bash
git clone [https://github.com/sunny07-stack/text-to-sql-ai.git](https://github.com/sunny07-stack/text-to-sql-ai.git)
cd text-to-sql-ai
```

### 2. Set up the virtual environment
```bash
python -m venv venv

# Windows PowerShell:
venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key
Set your Gemini API key in your terminal environment:

```powershell
# Windows PowerShell
$env:GEMINI_API_KEY="your_api_key_here"

# Linux/macOS
export GEMINI_API_KEY="your_api_key_here"
```

### 5. Launch the app
```bash
streamlit run app.py
```