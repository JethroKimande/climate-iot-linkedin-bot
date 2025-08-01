import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Default dataset produced by ``fetch_satellite_data.py``
DATA_FILE = "data/no2_comparison_data.csv"
CHART_DIR = "charts/"

def load_data():
    if not os.path.exists(DATA_FILE):
        print("❌ Data file not found.")
        return pd.DataFrame()
    return pd.read_csv(DATA_FILE)

def plot_pollution_trend(df):
    if df.empty:
        return

    plt.figure(figsize=(10, 6))

    if 'api_no2' in df.columns and df['api_no2'].notna().any():
        plt.plot(df['date'], df['api_no2'], marker='o', linestyle='-', color='blue', label='API NO₂')

    if 'image_no2' in df.columns:
        plt.plot(df['date'], df['image_no2'], marker='x', linestyle='-', color='darkred', label='Image NO₂')

    plt.title("🛰️ NO₂ Pollution Trend - Nairobi")
    plt.xlabel("Date")
    plt.ylabel("NO₂ (µg/m³)")
    plt.grid(True)
    plt.legend()

    os.makedirs(CHART_DIR, exist_ok=True)
    chart_path = os.path.join(CHART_DIR, f"no2_trend_{datetime.date.today()}.png")
    plt.savefig(chart_path)
    plt.close()

    print(f"✅ Chart saved: {chart_path}")
    return chart_path

def main():
    df = load_data()
    plot_pollution_trend(df)

if __name__ == "__main__":
    main()
