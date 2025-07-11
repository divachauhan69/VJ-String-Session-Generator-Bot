from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "20210909"))
API_HASH = environ.get("API_HASH", "0f171ff5fcac02ac7f43be4c5e7e1c09")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "8006975478")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002626222965")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://tabolo8539:0evqZDV4fC5fD17c@cluster0.cw8zxus.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
