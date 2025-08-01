from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import importlib
import logging

app = FastAPI()
scheduler = BackgroundScheduler()
scheduler.start()

# Logging setup
logging.basicConfig(filename='job_logs.txt', level=logging.INFO)


def run_job_by_name(job_name: str):
    try:
        module = importlib.import_module(f"scripts.{job_name}")
        module.main()
        logging.info(f"✅ Successfully ran {job_name}")
        return {"status": "success", "job": job_name}
    except Exception as e:
        logging.error(f"❌ Error in job {job_name}: {e}")
        return {"status": "error", "details": str(e)}


@app.post("/run-job/{job_name}")
def run_job(job_name: str):
    return run_job_by_name(job_name)
