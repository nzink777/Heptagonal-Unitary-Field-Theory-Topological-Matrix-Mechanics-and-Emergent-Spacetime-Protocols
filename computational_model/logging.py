"""
logging.py
Handles system telemetry and simulation logging for the HTFT framework.
"""
import logging
import os
from pathlib import Path
from datetime import datetime

# Path Configuration: Points to the Technomouse folder
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "Technomouse" / "Logs"

def setup_simulation_logger(session_name="HTFT_Session"):
    """
    Initializes a logger that saves to the Technomouse directory.
    """
    # Ensure the Technomouse log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"{session_name}_{timestamp}.log"
    
    # Configure the logger
    logger = logging.getLogger(session_name)
    logger.setLevel(logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger, log_file
  
