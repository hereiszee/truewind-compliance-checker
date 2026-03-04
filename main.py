import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("Truewind Nonprofit Compliance Checker")

desc = st.text_area("Transaction Description")
amount = st.number_input("Amount ($)", min_value=0.0)
category = st.selectbox("Category", ["Donation", "Expense", "Grant", "Other"])

if st.button("Check Compliance"):
    prompt = f"Check if this nonprofit transaction complies with IRS/GAAP: Description: {desc}, Amount: {amount}, Category: {category}. Provide yes/no and brief explanation."
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",  # or "mixtral-8x7b-32768" / "gemma2-9b-it" etc.
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    st.write(result)

email = st.text_input("Email for full report & Truewind demo")
if email:
    st.success("Report sent! Check inbox for Truewind integration info.")
