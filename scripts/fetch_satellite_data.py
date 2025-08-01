import requests
import datetime
import os
import time
import logging
import sys
import io
from PIL import Image
import numpy as np
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configurations
LAYER = "MODIS_Terra_Aerosol"
BASE_URL = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
API_URL = "https://api.caeli.io/v1/no2"  # Replace with actual endpoint
OUTPUT_DIR = "data/"
REGION = "36.65,-0.40,36.95,-0.10"
DATES = ["2025-07-01", "2025-07-08", "2025-07-15"]
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(OUTPUT_DIR, "fetch_logs.txt"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

def build_wms_url(date_str):
    return {
        "SERVICE": "WMS",
        "REQUEST": "GetMap",
        "VERSION": "1.3.0",
        "LAYERS": LAYER,
        "CRS": "EPSG:4326",
        "BBOX": REGION,
        "WIDTH": "1024",
        "HEIGHT": "1024",
        "FORMAT": "image/png",
        "TIME": date_str
    }

def fetch_image(date_str):
    params = build_wms_url(date_str)
    filename = os.path.join(OUTPUT_DIR, f"pollution_{date_str}.png")
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            logging.info(f"✅ Saved image for {date_str}")
            return filename
    except Exception as e:
        logging.error(f"❌ Failed to fetch image for {date_str}: {e}")
    return None

def estimate_no2_from_image(image_path):
    img = Image.open(image_path).convert("L")
    arr = np.array(img)
    mean_intensity = np.mean(arr)
    return round((mean_intensity / 255) * 40, 1)

def fetch_api_no2(date_str):
    try:
        response = requests.get(API_URL, params={"date": date_str, "bbox": REGION}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            value = data.get("no2_ppb")
            # API sometimes returns null, avoid rounding in that case
            return round(value, 1) if value is not None else None
    except Exception as e:
        logging.warning(f"⚠️ API fetch failed for {date_str}: {e}")
    return None

def save_to_csv(date_str, image_val, api_val):
    csv_path = os.path.join(OUTPUT_DIR, "no2_comparison_data.csv")
    write_header = not os.path.exists(csv_path)
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["date", "image_no2", "api_no2"])
        writer.writerow([date_str, image_val, api_val])

def main():
    for date in DATES:
        img_path = fetch_image(date)
        image_val = estimate_no2_from_image(img_path) if img_path else None
        api_val = fetch_api_no2(date)
        save_to_csv(date, image_val, api_val)
        print(f"{date}: Image={image_val} ppb, API={api_val} ppb")

if __name__ == "__main__":
    main()
