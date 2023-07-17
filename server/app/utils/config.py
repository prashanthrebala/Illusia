import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.environ.get("MONGO_URL")
IMAGE_GENERATION_ENDPOINT = os.environ.get("IMAGE_GENERATION_ENDPOINT")
X_RAPID_API_KEY = os.environ.get("X_RAPID_API_KEY")
X_RAPID_API_HOST = os.environ.get("X_RAPID_API_HOST")
DEFAULT_IMAGE_SIZE = os.environ.get("DEFAULT_IMAGE_SIZE")
DEFAULT_IMAGE_COUNT = 1

IMAGE_KIT_URL_ENDPOINT = os.environ.get("IMAGE_KIT_URL_ENDPOINT")
IMAGE_KIT_PRIVATE_KEY = os.environ.get("IMAGE_KIT_PRIVATE_KEY")
IMAGE_KIT_PUBLIC_KEY = os.environ.get("IMAGE_KIT_PUBLIC_KEY")
