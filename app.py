import sqlite3
import streamlit as st
import google.generativeai as genai
import os

st.title("🤖 Quick Text-to-SQL Analytics Assistant")
st.write("Ask questions about your company database in plain English!")

# Configure Gemini with your API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

user_question = st.text_input(
    "What would you like to know?",
    placeholder="e.g., Show me all employees",
)

if user_question:
  try:
    with st.spinner("Translating to SQL and querying database..."):
      # Initialize the fast and free Gemini 1.5 Flash model
      model = genai.GenerativeModel("gemini-3.8-flash")
      
      prompt = f"""
            You are a SQLite expert. Given the following database schema:
            - Table: employees (id INTEGER, name TEXT, department TEXT, salary INTEGER)
            - Table: sales (sale_id INTEGER, employee_id INTEGER, amount INTEGER, month TEXT)
            
            Write ONLY a valid SQLite query to answer this question: "{user_question}". 
            Do not include markdown ticks like ```sql, just output the raw SQL query.
            """

      # Send the prompt to Gemini
      response = model.generate_content(prompt)
      
      # Clean up the text just in case Gemini includes code formatting ticks
      sql_query = response.text.replace("```sql", "").replace("```", "").strip()

      st.subheader("Generated SQL Query:")
      st.code(sql_query, language="sql")

      conn = sqlite3.connect("company.db")
      cursor = conn.cursor()
      cursor.execute(sql_query)
      result = cursor.fetchall()
      conn.close()

      st.subheader("Query Result:")
      st.write(result)

  except Exception as e:
    st.error(f"An error occurred: {e}")