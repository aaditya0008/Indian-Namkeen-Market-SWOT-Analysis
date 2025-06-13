import pandas as pd

def run_kpi(params):
    file_path = params.get("file_path", "Market_data/KPI-15.csv")
    df = pd.read_csv(file_path, skiprows=2)
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all')
    df['Threat Level (High/Medium/Low)'] = df['Threat Level (High/Medium/Low)'].fillna('Unknown')
    threat_counts = df['Threat Level (High/Medium/Low)'].value_counts().to_dict()
    return {
        "kpi_name": "Private Label Threat Levels",
        "threat_summary": threat_counts,
        "total_records": len(df)
    }