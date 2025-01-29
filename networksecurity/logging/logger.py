import logging
import os
from datetime import datetime

# Define the logs directory
log_dir = os.path.join(os.getcwd(), "logs")

# Ensure the logs directory exists
os.makedirs(log_dir, exist_ok=True)  

# Create log file path
log_file = f"{datetime.now().date().strftime('%m_%d_%Y')}.log"
log_file_path = os.path.join(log_dir, log_file)

# Ensure log file exists before setting permissions
if not os.path.exists(log_file_path):
    with open(log_file_path, "w"):  # Create empty log file
        pass  

# Set permissions (optional)
os.chmod(log_file_path, 0o764)  

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Test log
#logging.info("Logging setup successful!")
#print(f"Logging to: {log_file_path}")
