"""Configuration loader for API keys and environment variables."""

import os
import sys
from dotenv import load_dotenv


def get_api_key() -> str:
    """
    Load and return the Google API key from environment variables.
    
    Returns:
        str: The Google API key.
        
    Exits:
        Exits with code 1 if the API key is missing or empty.
    """
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key or api_key.strip() == "":
        sys.stderr.write("Error: GOOGLE_API_KEY not found in environment.\n")
        sys.stderr.write("Please create a .env file with: GOOGLE_API_KEY=your_key_here\n")
        sys.exit(1)
    
    return api_key.strip()
