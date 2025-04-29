from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file once

PROXY_API_KEY = os.getenv("PROXY_API_KEY")
PROXY_BASE_URL = os.getenv("PROXY_BASE_URL")
