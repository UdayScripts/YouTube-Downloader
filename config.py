import os

class Config:
    API_ID = int(os.getenv("API_ID", '22548817'))
    API_HASH = os.getenv("API_HASH", '759cad1d21c26b8dcee11f634df37e72')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '5530115227:AAEabF7sgjh3u4fFN1o01FtYkm1wZBwJ7QI')
