import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Truewind Nonprofit Compliance Checker")

desc = st.text_area("Transaction Description")
amount = st.number_input("Amount ($)", min_value=0.0)
category = st.selectbox("Category", ["Donation", "Expense", "Grant", "Other"])

if st.button("Check Compliance"):
    prompt = f"Check if this nonprofit transaction complies with IRS/GAAP: Description: {desc}, Amount: {amount}, Category: {category}. Provide yes/no and brief explanation."
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    result = response.choices[0].message.content
    st.write(result)
    
    email = st.text_input("Email for full report & Truewind demo")
    if email:
        st.success("Report sent! Check inbox for Truewind integration info.")
