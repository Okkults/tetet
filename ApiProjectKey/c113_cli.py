"""Main CLI entrypoint for c113-cli trading decision tool."""

import argparse
import sys
import time
from config import get_api_key
from ai_client import run_multimodal_inference
from utils import extract_text_from_response, reduce_to_decision


def main() -> None:
    """
    Main function that orchestrates the CLI workflow.
    
    Parses arguments, calls the AI API, and outputs the decision.
    """
    parser = argparse.ArgumentParser(
        description="AI-powered trading decision CLI using Google Gemini Vision"
    )
    parser.add_argument(
        "--image",
        type=str,
        required=True,
        help="Path to the screenshot/image file"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="The instruction/prompt for the AI model"
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="decision",
        choices=["raw", "decision"],
        help="Output mode: 'raw' for full response, 'decision' for LONG/SHORT (default: decision)"
    )
    
    args = parser.parse_args()
    
    try:
        start_time = time.time()
        
        api_key = get_api_key()
        
        response = run_multimodal_inference(api_key, args.prompt, args.image)
        
        model_text = extract_text_from_response(response)
        
        if args.mode == "decision":
            final_output = reduce_to_decision(model_text)
        else:
            final_output = model_text.strip()
        
        print(final_output)
        
        elapsed = time.time() - start_time
        sys.stderr.write(f"[latency {elapsed:.2f}s]\n")
        
        sys.exit(0)
        
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
