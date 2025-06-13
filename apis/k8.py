import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

def load_and_process_data(file_path):
    try:
        df = pd.read_csv(file_path, skiprows=2)
        df.columns = [
            "Platform", "Product_Name", "Brand", "Weight_g", "Price_INR",
            "Discount_Percent", "Availability", "Delivery_Time", "Product_Link"
        ]

        df["Availability"] = df["Availability"].str.strip().str.lower()

        def rate_availability(val):
            if val == "in stock":
                return "High"
            elif val == "out of stock":
                return "Low"
            else:
                return "Medium"

        df["Qualitative_Rating"] = df["Availability"].apply(rate_availability)

        return df

    except Exception as e:
        print(f"Error processing file: {e}")
        return None


def generate_heatmap_chart_base64(df):
    try:
        summary = df.groupby("Platform")["Qualitative_Rating"].value_counts().unstack(fill_value=0)

        plt.figure(figsize=(8, 5))
        sns.heatmap(summary, annot=True, cmap="YlGnBu", fmt="d", linewidths=.5, cbar=False)

        plt.title("📊 Platform-wise Product Availability Ratings")
        plt.xlabel("Rating")
        plt.ylabel("Platform")
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)

        return base64.b64encode(buf.read()).decode("utf-8")

    except Exception as e:
        print(f"Error generating heatmap: {e}")
        return None


def run_kpi(params):
    file_path = params.get("file_path", "Market_data/KPI-8.csv")
    df = load_and_process_data(file_path)

    if df is not None and not df.empty:
       
        high_count = df[df["Qualitative_Rating"] == "High"].shape[0]
        medium_count = df[df["Qualitative_Rating"] == "Medium"].shape[0]
        low_count = df[df["Qualitative_Rating"] == "Low"].shape[0]

        return {
            "kpi_name": "Platform-wise Availability Ratings",
            "records_count": len(df),
            "rating_counts": {
                "High": high_count,
                "Medium": medium_count,
                "Low": low_count
            },
            
        }
    else:
        return {
            "kpi_name": "Platform-wise Availability Ratings",
            "error": "Failed to load or process data"
        }


def get_plot_image(file_path):
    """
    Returns a PNG image buffer of the platform-wise product availability heatmap.
    """
    df = load_and_process_data(file_path)
    if df is None or df.empty:
        raise FileNotFoundError("Failed to load or process data")
    summary = df.groupby("Platform")["Qualitative_Rating"].value_counts().unstack(fill_value=0)

    plt.figure(figsize=(8, 5))
    sns.heatmap(summary, annot=True, cmap="YlGnBu", fmt="d", linewidths=.5, cbar=False)
    plt.title("📊 Platform-wise Product Availability Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Platform")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf