import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


DATA_FILE = "data/processed_pollution.csv"  # Adjust as needed
CHART_DIR = "charts/"

def load_data():
    if not os.path.exists(DATA_FILE):
        print("❌ Processed data file not found.")
        return pd.DataFrame()
    return pd.read_csv(DATA_FILE)

def plot_pollution_trend(df):
    if df.empty:
        return

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['no2'], marker='o', linestyle='-', color='darkred')
    plt.title("🛰️ NO₂ Pollution Trend - Nairobi")
    plt.xlabel("Date")
    plt.ylabel("NO₂ (µg/m³)")
    plt.grid(True)

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
