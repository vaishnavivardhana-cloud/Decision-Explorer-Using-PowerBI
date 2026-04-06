import streamlit as st

st.title("📊 Business Insights Dashboard")

category = st.session_state.get("category")
company = st.session_state.get("company")

# Safety check
if not category or not company:
    st.warning("Please go back and select category & company")
    st.stop()

# Power BI links
dashboard_links = {
    "Retail": "https://app.powerbi.com/reportEmbed?reportId=8d2179c2-0967-40ff-b2ba-0124026dbe49&autoAuth=true&ctid=a01ef85e-a667-4caf-905e-72703b6785b9",
    "SaaS": "https://app.powerbi.com/reportEmbed?reportId=6af3576c-7192-42c0-b606-50cab53524a2&autoAuth=true&ctid=a01ef85e-a667-4caf-905e-72703b6785b9",
    "Fintech": "https://app.powerbi.com/reportEmbed?reportId=343f0892-122e-43d3-87d0-cb926ed31172&autoAuth=true&ctid=a01ef85e-a667-4caf-905e-72703b6785b9",
    "Enterprise": "https://app.powerbi.com/reportEmbed?reportId=b30f170e-3ebf-44fa-8cb0-94deb6aa7c6b&autoAuth=true&ctid=a01ef85e-a667-4caf-905e-72703b6785b9"
}

base_url = dashboard_links.get(category)

if not base_url:
    st.error("Invalid category")
    st.stop()

# Filter (IMPORTANT: match column name exactly in Power BI)
filtered_url = f"{base_url}?filter=Company eq '{company}'"

st.success(f"Showing insights for {company}")

st.components.v1.iframe(
    filtered_url,
    height=650,
    width=1200
)