from flask import Flask, request, jsonify
import streamlit as st
from src.agent import SalesAgent

app = Flask(__name__)
agent = SalesAgent()

def main():
    st.title("SalesCopilot - AI-Powered Sales Assistant")
    
    customer_query = st.text_input("Customer Query:")
    if st.button("Get Response"):
        if customer_query:
            response = agent.get_response(customer_query)
            st.write("Salesperson's Response:", response)
        else:
            st.write("Please enter a customer query.")

if __name__ == "__main__":
    main()