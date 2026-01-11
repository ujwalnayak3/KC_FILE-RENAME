import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25953006")

API_HASH = os.environ.get("API_HASH", "d5850aeef7dd3d01fe6b698c0a0d4be8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1003187473140") 

DB_NAME = os.environ.get("DB_NAME","kfcinemas")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Kfcinemas:ujwal@cluster0.olxb2bz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1981280736').split()]

PORT = os.environ.get("PORT", "8080")

