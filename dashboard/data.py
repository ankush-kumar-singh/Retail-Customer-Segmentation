# ==========================================
# Data Loader
# ==========================================

from pathlib import Path
import pandas as pd


# ==========================================
# Project Root
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# Dataset Path
# ==========================================

DATA_PATH = BASE_DIR / "datasets" / "rfm_main.csv"

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(DATA_PATH)
print(df.dtypes)

# ==========================================
# KPI Values
# ==========================================

total_customers = df["Customer ID"].nunique()

total_revenue = df["Monetary"].sum()

avg_monetary = round(df["Monetary"].mean(), 2)

champions = (df["Segment"] == "Champions").sum()

# ==========================================
# Segment Distribution
# ==========================================

segment_counts = (
    df["Segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    "Segment",
    "Customers"
]