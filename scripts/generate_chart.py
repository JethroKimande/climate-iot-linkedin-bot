import pandas as pd
import os
import datetime
import sys
import io
from typing import Optional, Union
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Try to import matplotlib, fallback to basic plotting if not available
matplotlib_available = False
plt = None
try:
    import matplotlib.pyplot as plt
    matplotlib_available = True
except ImportError:
    print("⚠️ matplotlib not available, will create basic text output instead")


# Default dataset produced by ``fetch_satellite_data.py``
DATA_FILE = "data/no2_comparison_data.csv"
CHART_DIR = "charts/"


def load_data() -> pd.DataFrame:
    if not os.path.exists(DATA_FILE):
        print("❌ Data file not found.")
        return pd.DataFrame()
    return pd.read_csv(DATA_FILE)


def plot_pollution_trend(df: pd.DataFrame) -> Optional[Union[str, None]]:
    if df.empty:
        print("❌ No data available for plotting")
        return None

    if not matplotlib_available:
        # Fallback: create a simple text-based chart
        print("📊 NO₂ Pollution Trend - Nairobi (Text Format)")
        print("=" * 50)
        for _, row in df.iterrows():
            api_val = row.get('api_no2', 'N/A')
            img_val = row.get('image_no2', 'N/A')
            print(f"Date: {row['date']} | API NO₂: {api_val} ppb | Image NO₂: {img_val} ppb")
        print("=" * 50)
        return "text_chart"

    # Original matplotlib plotting
    if plt is not None:
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
    else:
        print("❌ matplotlib not available for plotting")
        return None

    print(f"✅ Chart saved: {chart_path}")
    return chart_path


def main():
    df = load_data()
    plot_pollution_trend(df)


if __name__ == "__main__":
    main()
