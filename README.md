# 🌍 Climate-IoT LinkedIn Automation Bot

A Python-based automation system that fetches satellite air pollution data, processes it into insights, visualizes trends, and posts weekly updates to LinkedIn—all powered by open data.
📡 Powered by APIs like Caeli and NASA GIBS 📊 Visualizes pollution metrics via Python charts 📢 Auto-publishes commentary through LinkedIn UGC API 🧠 Designed for collaboration, impact, and scalability
## 🚀 Overview

This project automates the pipeline between open satellite APIs and professional social media. It analyzes pollutants like NO₂, shares the story through charts and captions, and posts to LinkedIn using scheduled routines. Perfect for climate advocacy, data storytelling, and building your public voice.

## 📁 Folder Structure

/climate-iot-linkedin-bot
├── apscheduler_api/               # API endpoints for job scheduling
├── data/                          # Data and log files
├── scripts/
│   ├── fetch_satellite_data.py    # Download images and NO₂ estimates
│   ├── generate_chart.py          # Build pollution trend charts
│   └── list_gibs_layers.py        # List available NASA GIBS layers
├── job_logs.txt                   # Example job log output
├── requirements.txt
└── README.md


## 🛰️ Data Sources

- [Caeli API](https://caeli.nl/en/api/) – satellite-based NO₂, CO, O₃, SO₂ data
- [NASA Earthdata (GIBS)](https://earthdata.nasa.gov/) – global air quality maps
- Others optional: OpenWeather Pollution API, Sentinel Hub

## 🧰 Dependencies

- Python 3.9+
- `requests`
- `schedule`
- `matplotlib`
- `python-dotenv`
- `pandas`

```bash
pip install -r requirements.txt


🔐 Environment Variables
Create a .env file with:
LINKEDIN_ACCESS_TOKEN=your_token_here
CAELI_API_KEY=your_api_key_here

⏰ Automation Schedule
Posts run every Monday at 09:00 AM. Adjust this in scheduler.py as needed.

## 🧪 Running Tests

Install the requirements first, then run `pytest` from the project root:

```bash
pytest
```

📢 Sample LinkedIn Output
🌫️ This week’s NO₂ average over Nairobi: 18.6 µg/m³. Satellite data confirms a 12% drop compared to last week. Could rainfall be clearing the air? Let's talk about climate resilience. #ClimateTech #DataForGood #IoTAfrica

🤝 Contributing
Open to collaboration:

Add support for PM2.5, O₃, CO metrics

Map data using GeoJSON or satellite overlays

Translate insights into infographics

Expand automation to multiple regions

📜 License
MIT © 2025 Jethro

---

If you’d like a visual badge setup, GitHub Actions CI trigger, or even a contributor’s guide section, I can snap those in next. Want to keep evolving this into a full-blown dashboard or newsletter tool? I’m ready when you are! 😎📈

