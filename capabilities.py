import os
from dotenv import load_dotenv

load_dotenv('.env')
url = os.getenv("RARIBLE_URL")