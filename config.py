import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("AIzaSyAV43hcTjOnzete3grud2bEAcSUv1aE2xo")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")
