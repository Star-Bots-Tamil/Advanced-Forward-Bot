import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", 11973721))
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6460834619:AAHyB5jkF2QXpSaCW620YmbdvFVztfcHwSM")

# Pyrogram session name
SESSION_NAME = os.environ.get("SESSION_NAME")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
