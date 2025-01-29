import logging
import os
from datetime import datetime

log_file = f"{datetime.now().date().strftime('%m_%d_%Y_%H_%M_%S').log}"

log_file_path  = os.path.join(os.getcwd(),"logs",log_file)

if not os.path.exists(log_file_path):
    os.makedirs(log_file_path,exist_ok=True)


logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
