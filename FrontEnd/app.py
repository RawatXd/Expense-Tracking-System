import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"
st.title("Expense Tracking System")

tab1,tab2 = st.tabs(["Add /Update","Analytics"])

with tab1:
    selected_date = st.date_input("Enter Date",datetime(2024,8,1),label_visibility="collapsed")
    response = requests.get(f'{API_URL}/expenses/{selected_date}')
    if response.status_code == 200:
        existing_expenses = response.json()
        st.write(existing_expenses)
    else:
        st.error("Failed to retrieve expenses")
        existing_response =[]

    categories = ["Rent","Food","Shopping","Entertainment","Other"]

    with st.form(key="expense_form"):
        for i in range(5):
            col1,col2,col3 = st.columns(3)
            with col1:
                st.number_input("Amount",min_value=0.0,value=0.0,step=1.0,key =f"amount {i}")
            with col2:
                st.selectbox(label ="Category",options=categories,key =f"category_{i}")
            with col3:
                notes_input = st.text_input(label ="",value ="",key =f"notes_{i}")


        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            pass