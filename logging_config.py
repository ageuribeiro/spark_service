import logging
import logging_config
import json
import os


# Directory and files logs
LOG_DIR = 'logs'
LOG_FILE = 'app.log'
JSON_LOG_FILE = 'app.json'

# Create of directory de logs
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Config logging
LOGGING_CONFIG = {
    "version":  1,
    "disable_existing_loggers": False,
    "formatters":{
        "standard":{
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        }
    },
    "handlers":{
        "file_handler":{
            "class": "logging.FileHandler",
            "formatter": "standard",
            "filename": os.path.join(LOG_DIR, LOG_FILE),
            "level": "DEBUG"
        },
        "json_handler":{
            "class": "logging.FileHandler",
            "formatter": "standard",
            "filename": os.path.join(LOG_DIR, JSON_LOG_FILE),
            "level": "DEBUG"
        }
    },
    "root":{
        "handlers": ["file_handler", "json_handler"],
        "level": "DEBUG"

    },
    "loggers":{
        "my_logger":{
            "handlers":["file_handler", "json_handler"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("my_logger")

# Function for save logs in JSON Format
def save_log_json(log_record):
    log_entry = {
        "timestamp": log_record.asctime,
        "name": log_record.name,
        "level": log_record.levelname,
        "message": log_record.message
    }

    with open(os.path.join(LOG_DIR, JSON_LOG_FILE), 'a') as json_log:
        json_log.write(json.dumps(log_entry) + '\n')

    