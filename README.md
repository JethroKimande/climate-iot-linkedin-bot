# 🌍 Climate-IoT LinkedIn Automation Bot

A Python-based automation system that fetches satellite air pollution data, processes it into insights, visualizes trends, and posts weekly updates to LinkedIn—all powered by open data.

📡 **Powered by APIs like Caeli and NASA GIBS**  
📊 **Visualizes pollution metrics via Python charts**  
📢 **Auto-publishes commentary through LinkedIn UGC API**  
🧠 **Designed for collaboration, impact, and scalability**

## 🚀 Overview

This project automates the pipeline between open satellite APIs and professional social media. It analyzes pollutants like NO₂, shares the story through charts and captions, and posts to LinkedIn using scheduled routines. Perfect for climate advocacy, data storytelling, and building your public voice.

## 📁 Folder Structure

```text
climate-iot-linkedin-bot/
├── apscheduler_api/          # FastAPI server for job automation
│   └── main.py              # API endpoints and job runner
├── scripts/                 # Core automation scripts
│   ├── fetch_satellite_data.py  # Downloads satellite imagery and API data
│   ├── generate_chart.py        # Creates pollution trend charts
│   ├── compose_linkedin_post.py # Generates LinkedIn post content
│   └── list_gibs_layers.py     # Lists available NASA GIBS layers
├── data/                    # Data storage directory
│   ├── no2_comparison_data.csv # Pollution data CSV
│   └── *.png                # Satellite imagery files
├── charts/                  # Generated chart outputs
├── logs/                    # Application logs
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## 🛰️ Data Sources

- **[Caeli API](https://caeli.nl/en/api/)** – satellite-based NO₂, CO, O₃, SO₂ data
- **[NASA Earthdata (GIBS)](https://earthdata.nasa.gov/)** – global air quality maps
- **Others optional:** OpenWeather Pollution API, Sentinel Hub

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Clone the repository
git clone <your-repo-url>
cd climate-iot-linkedin-bot

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy the environment template
cp .env.example .env

# Edit .env with your API keys
# LINKEDIN_ACCESS_TOKEN=your_linkedin_token
# CAELI_API_KEY=your_caeli_api_key
```

### 3. Run Individual Scripts

```bash
# Fetch satellite data
python scripts/fetch_satellite_data.py

# Generate charts
python scripts/generate_chart.py

# Compose LinkedIn post
python scripts/compose_linkedin_post.py
```

### 4. Start the API Server

```bash
# Start the FastAPI server
uvicorn apscheduler_api.main:app --reload

# Test the API
curl -X POST http://localhost:8000/run-job/compose_linkedin_post
```

## 🔐 Environment Variables

Create a `.env` file with the following variables:

```env
# LinkedIn API Configuration
LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token_here

# Caeli API Configuration  
CAELI_API_KEY=your_caeli_api_key_here

# Optional: Redis Configuration
REDIS_URL=redis://localhost:6379

# Optional: Logging Level
LOG_LEVEL=INFO
```

## ⏰ Automation Schedule

Posts run every Monday at 09:00 AM. Adjust this in scheduler.py as needed.

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_fetch_satellite.py
```

## 📊 Sample Output

### LinkedIn Post Example

```text
🛰️ Weekly NO₂ update over Nairobi
Date: 2025-07-15
Satellite estimate: 4.3 ppb
#ClimateTech #DataForGood #IoTAfrica
```

### Chart Generation

The system generates pollution trend charts showing satellite vs API data comparisons.

## 🔧 API Endpoints

When running the FastAPI server, you can access:

- `GET /` - API information
- `GET /health` - Health check
- `POST /run-job/{job_name}` - Execute a script

Available job names:

- `fetch_satellite_data` - Download satellite imagery and API data
- `generate_chart` - Create pollution trend charts  
- `compose_linkedin_post` - Generate LinkedIn post content
- `list_gibs_layers` - List available NASA GIBS layers

## 🤝 Contributing

Open to collaboration! Areas for improvement:

- ✅ Add support for PM2.5, O₃, CO metrics
- ✅ Map data using GeoJSON or satellite overlays  
- ✅ Translate insights into infographics
- ✅ Expand automation to multiple regions
- ✅ Add LinkedIn posting automation
- ✅ Implement data caching and optimization

## 🐛 Troubleshooting

### Common Issues

1. **Matplotlib Import Error**: The system includes fallback text output if matplotlib fails
2. **API Connection Issues**: Check your internet connection and API keys
3. **Missing Data**: Ensure the `data/` directory exists and has proper permissions

### Logs

Check the `logs/job_logs.txt` file for detailed execution logs.

## 📜 License

MIT © 2025 Jethro

---

## 🚀 Next Steps

Want to evolve this into a full-blown dashboard or newsletter tool? The foundation is ready for:

- 📈 Real-time dashboard with web interface
- 📧 Email newsletter automation  
- 🔄 Multi-region data collection
- 📱 Mobile app integration
- 🤖 Advanced AI-powered insights

Ready when you are! 😎📈
