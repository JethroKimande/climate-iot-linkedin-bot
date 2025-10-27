from fastapi import FastAPI, HTTPException
from apscheduler.schedulers.background import BackgroundScheduler
import importlib
import logging
import os
from datetime import datetime

app = FastAPI(title="Climate IoT LinkedIn Bot API", version="1.0.0")
scheduler = BackgroundScheduler()
scheduler.start()

# Logging setup
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/job_logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def run_job_by_name(job_name: str):
    try:
        # Check if script exists
        script_path = f"scripts/{job_name}.py"
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Script {script_path} not found")

        module = importlib.import_module(f"scripts.{job_name}")
        if not hasattr(module, 'main'):
            raise AttributeError(f"Script {job_name} does not have a main() function")

        start_time = datetime.now()
        module.main()
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        logging.info(f"✅ Successfully ran {job_name} in {duration:.2f}s")
        return {"status": "success", "job": job_name, "duration": f"{duration:.2f}s"}
    except Exception as e:
        logging.error(f"❌ Error in job {job_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Job {job_name} failed: {str(e)}")


@app.get("/")
def root():
    return {"message": "Climate IoT LinkedIn Bot API", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/run-job/{job_name}")
def run_job(job_name: str):
    return run_job_by_name(job_name)
