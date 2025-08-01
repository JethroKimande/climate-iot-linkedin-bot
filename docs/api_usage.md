# API Usage

This project bundles a minimal FastAPI app so you can run the automation scripts on demand.

## Start the server

Install the requirements and start Uvicorn pointing at the app:

```bash
pip install -r requirements.txt
uvicorn apscheduler_api.main:app --reload
```

The server will run on <http://localhost:8000> by default.

## Trigger a job

Send a POST request to `/run-job/{job_name}` where `job_name` matches a Python script inside the `scripts/` folder. Example:

```bash
curl -X POST http://localhost:8000/run-job/fetch_satellite_data
```

The API responds with `{"status": "success", "job": "fetch_satellite_data"}` if the job completes without raising an exception.

## Available jobs

Below are the job names you can call and what each script does:

- `fetch_satellite_data` – Downloads NO₂ satellite imagery from NASA GIBS, pulls matching data from the Caeli API and stores comparisons in `data/no2_comparison_data.csv`.
- `generate_chart` – Reads `data/processed_pollution.csv` and generates a trend chart saved in `charts/`.
- `list_gibs_layers` – Lists all map layers provided by the NASA GIBS WMS service.
- `ptest` – Monitors network connectivity and attempts router reboot and DNS flush if the connection fails.

