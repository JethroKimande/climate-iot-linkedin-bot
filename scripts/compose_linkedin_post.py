import os
import pandas as pd
import datetime

data_file = os.path.join('data', 'no2_comparison_data.csv')


def load_data():
    if not os.path.exists(data_file):
        return pd.DataFrame()
    return pd.read_csv(data_file)


def compose_caption(df: pd.DataFrame) -> str:
    if df.empty:
        return "No data available to compose a LinkedIn post."
    df = df.dropna(subset=['date'])
    if df.empty:
        return "No valid data found."
    latest = df.iloc[-1]
    date_str = latest['date']
    img_val = latest.get('image_no2', '')
    api_val = latest.get('api_no2', '')
    caption_lines = [
        "🛰️ Weekly NO₂ update over Nairobi",
        f"Date: {date_str}",
        f"Satellite estimate: {img_val} ppb",
    ]
    if pd.notna(api_val) and str(api_val) != "":
        caption_lines.append(f"Caeli API: {api_val} ppb")
    caption_lines.append("#ClimateTech #DataForGood #IoTAfrica")
    return "\n".join(caption_lines)


def main():
    df = load_data()
    caption = compose_caption(df)
    print(caption)


if __name__ == "__main__":
    main()
