import pandas as pd

def get_companies(category):
    file_map = {
        "Retail": "data/P2_retail_dataset.xlsx",
        "SaaS": "data/P2_saas_dataset.xlsx",
        "Fintech": "data/P2_fintech_dataset.xlsx",
        "Enterprise": "data/P2_enterprise_dataset.xlsx"
    }

    file_path = file_map.get(category)

    if not file_path:
        return []

    df = pd.read_excel(file_path)

    if "Company" not in df.columns:
        return []

    return sorted(df["Company"].dropna().unique())