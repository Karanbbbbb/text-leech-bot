import os

API_ID    = os.environ.get("API_ID", "28274437")
API_HASH  = os.environ.get("API_HASH", "6554efd9d72c95f3fdd600d76e37ed53")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
