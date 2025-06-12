import streamlit as st
from tools.fetch_stock_info import Anazlyze_stock

st.set_page_config(page_title="Stock Analyzer", layout="wide")
st.title("📊 Stock Analyzer")

query = st.text_input("Enter Stock Name or Ticker (e.g., RELIANCE.NS):")

if query:
    with st.spinner("Analyzing..."):
        try:
            result = Anazlyze_stock(query)
            st.markdown(result, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")