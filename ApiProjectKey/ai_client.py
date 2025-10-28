"""Client for calling Google Gemini Vision API."""

import requests
from typing import Dict
from utils import encode_image_to_base64


def run_multimodal_inference(api_key: str, prompt: str, image_path: str) -> Dict:
    """
    Run multimodal inference using Google Gemini Vision API.
    
    Args:
        api_key: The Google API key for authentication.
        prompt: The text prompt/instruction for the AI.
        image_path: Path to the image file to analyze.
        
    Returns:
        The parsed JSON response as a Python dictionary.
        
    Raises:
        RuntimeError: If the API call fails (non-200 status code).
        FileNotFoundError: If the image file doesn't exist.
    """
    base64_image, mime_type = encode_image_to_base64(image_path)
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    request_body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": base64_image
                        }
                    }
                ]
            }
        ]
    }
    
    response = requests.post(url, json=request_body)
    
    if response.status_code != 200:
        raise RuntimeError(
            f"API call failed with status {response.status_code}: {response.text}"
        )
    
    return response.json()
