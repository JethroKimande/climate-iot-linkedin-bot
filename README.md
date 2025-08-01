# 🌍 Climate-IoT LinkedIn Automation Bot

A Python-based automation system that fetches satellite air pollution data, processes it into insights, visualizes trends, and posts weekly updates to LinkedIn—all powered by open data.
📡 Powered by APIs like Caeli and NASA GIBS 📊 Visualizes pollution metrics via Python charts 📢 Auto-publishes commentary through LinkedIn UGC API 🧠 Designed for collaboration, impact, and scalability
## 🚀 Overview

This project automates the pipeline between open satellite APIs and professional social media. It analyzes pollutants like NO₂, shares the story through charts and captions, and posts to LinkedIn using scheduled routines. Perfect for climate advocacy, data storytelling, and building your public voice.

## 📁 Folder Structure

<<<<<<< HEAD
```
.
├── apscheduler_api/  # FastAPI server for running jobs
│   └── main.py
├── scripts/          # Stand‑alone job scripts
│   ├── fetch_satellite_data.py
│   ├── generate_chart.py
│   ├── list_gibs_layers.py
│   └── ptest.py
├── data/             # Output CSVs and images
├── job_logs.txt      # Logs from scheduled runs
├── requirements.txt  # Python dependencies
└── README.md
```

=======
>>>>>>> main

## 🛰️ Data Sources

- [Caeli API](https://caeli.nl/en/api/) – satellite-based NO₂, CO, O₃, SO₂ data
- [NASA Earthdata (GIBS)](https://earthdata.nasa.gov/) – global air quality maps
- Others optional: OpenWeather Pollution API, Sentinel Hub

## 🧰 Dependencies

This project requires **Python&nbsp;3.9+**. Install all packages with:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the repository root containing:

```
LINKEDIN_ACCESS_TOKEN=your_token_here
CAELI_API_KEY=your_api_key_here
```

These variables are read by the job scripts at runtime.


⏰ Automation Schedule
Posts run every Monday at 09:00 AM. Adjust this in `scheduler.py` as needed.

## 🚦 Running the API

Start the FastAPI server with:

```bash
uvicorn apscheduler_api.main:app --reload
```

Trigger an individual job (for example `fetch_satellite_data`) via HTTP:

```bash
curl -X POST http://127.0.0.1:8000/run-job/fetch_satellite_data
```

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

## Running the Job API

This repository includes a small FastAPI app that runs jobs defined in the
`scripts/` folder. Install the dependencies and launch it with:

```bash
uvicorn apscheduler_api.main:app --reload
```

Once running, trigger a job by sending a POST request to `/run-job/{job_name}`.
See [docs/api_usage.md](docs/api_usage.md) for a full list of jobs and example
commands.

If you’d like a visual badge setup, GitHub Actions CI trigger, or even a contributor’s guide section, I can snap those in next. Want to keep evolving this into a full-blown dashboard or newsletter tool? I’m ready when you are! 😎📈

