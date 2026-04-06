import streamlit as st
from data_handler import get_companies

st.set_page_config(page_title="Decision Explorer", layout="wide")

st.title("🚀 Decision Explorer")

# Step 1: Category
category = st.selectbox(
    "Select Business Category",
    ["Retail", "SaaS", "Fintech", "Enterprise"]
)

# Step 2: Info Popup
with st.expander("📊 How Data Analyst Helps"):
    st.write("""
    ✔ Identify revenue leaks  
    ✔ Improve customer retention  
    ✔ Optimize operations  
    ✔ Forecast future growth  
    """)

# Step 3: Company Dropdown
companies = get_companies(category)

company = st.selectbox(
    "Select Company",
    companies if companies else ["No companies available"]
)

# Step 4: Navigation
if st.button("🔍 Explore Insights"):
    if company == "No companies available":
        st.error("No company found")
    else:
        st.session_state["category"] = category
        st.session_state["company"] = company
        st.switch_page("pages/dashboard.py")