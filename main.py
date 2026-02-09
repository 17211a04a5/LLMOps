from dotenv import load_dotenv
import os
import uvicorn
import subprocess
import threading
import time
from app.common.logger import get_logger
from app.common.customException import CustomException
from app.config.settings import settings
from app.backend.api import app

load_dotenv()

logger = get_logger(__name__)

def run_api():
    try:
        logger.info("Starting FastAPI server...")
        subprocess.run(["uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", str(settings.API_PORT)])
    except CustomException as e:
        logger.error("Error starting FastAPI server")
        raise CustomException("Error starting FastAPI server", error_detail=e)

def run_frontend():
    try:
        logger.info("Starting Streamlit frontend...")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"],check=True)
    except CustomException as e:
        logger.error("Error starting Streamlit frontend", exc_info=True)
        raise CustomException("Error starting Streamlit frontend", error_detail=e)
    

if __name__ == "__main__":
    try:
        api_thread = threading.Thread(target=run_api, daemon=True)
        api_thread.start()

        # Wait for the API to start before launching the frontend
        time.sleep(5)

        run_frontend()
    except CustomException as e:
        logger.error("Error in main execution", exc_info=True)
        raise CustomException("Error in main execution", error_detail=e)