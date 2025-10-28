"""Utility functions for image encoding, response parsing, and decision extraction."""

import base64
import os
from typing import Tuple


def encode_image_to_base64(image_path: str) -> Tuple[str, str]:
    """
    Encode an image file to base64 and determine its MIME type.
    
    Args:
        image_path: Path to the image file.
        
    Returns:
        A tuple of (base64_string, mime_type).
        
    Raises:
        FileNotFoundError: If the image file doesn't exist.
        IOError: If the file cannot be read.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    _, ext = os.path.splitext(image_path.lower())
    
    if ext in ['.jpg', '.jpeg']:
        mime_type = "image/jpeg"
    elif ext == '.png':
        mime_type = "image/png"
    else:
        mime_type = "image/png"
    
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        base64_str = base64.b64encode(image_data).decode('utf-8')
    
    return base64_str, mime_type


def extract_text_from_response(resp: dict) -> str:
    """
    Extract the text content from a Gemini API response.
    
    Args:
        resp: The API response dictionary.
        
    Returns:
        The extracted text, or an empty string if not found.
    """
    try:
        text = resp["candidates"][0]["content"]["parts"][0]["text"]
        return text.strip()
    except (KeyError, IndexError, TypeError):
        return ""


def reduce_to_decision(raw: str) -> str:
    """
    Reduce AI response text to a simple trading decision (LONG or SHORT).
    
    Args:
        raw: The raw text response from the AI model.
        
    Returns:
        A single uppercase decision keyword, typically "LONG" or "SHORT".
    """
    lower_raw = raw.lower()
    
    if "long" in lower_raw and "short" not in lower_raw:
        return "LONG"
    
    if "short" in lower_raw and "long" not in lower_raw:
        return "SHORT"
    
    first_line = raw.split('\n')[0].strip()
    return first_line[:60].upper()
