from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("URL")

# Check if the API key is loaded
if GEMINI_API_KEY:
    print("GEMINI_API_KEY loaded successfully:", GEMINI_API_KEY[:5] + "****")  # Masking for security
else:
    print("Failed to load GEMINI_API_KEY")
