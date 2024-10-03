import os

class Config:
    API_ID = int(os.getenv("API_ID", '26383754'))
    API_HASH = os.getenv("API_HASH", 'f743596f09f383e7bbcc62ce62367f06')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '8183335872:AAEluCkzj-JhnMngkbfJNgeMAbLzMtF5Bwc')
