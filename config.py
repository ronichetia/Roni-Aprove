import os
from typing import List

API_ID = os.environ.get("API_ID", "39020336")
API_HASH = os.environ.get("API_HASH", "b6b6742ac6ad6936dfc88caeac95b7a4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8839051596:AAGrniVjLipqaFWoGO-WJa53CG2THRMgasI")
ADMIN = int(os.environ.get("ADMIN", "5953067512"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003819889662"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Maggie12:Deepta123@cluster0.g4syvio.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "approve")
IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "-1004215235663").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "-1004335653665").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
