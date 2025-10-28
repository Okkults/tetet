# c113-cli

A command-line tool for AI-powered trading decisions using Google Gemini Vision API. Analyze option chain screenshots and get instant LONG/SHORT trading signals directly in your terminal.

## Features

- 🖼️ **Image Analysis**: Feed screenshots of option chains, tape data, or any trading charts
- 🤖 **AI-Powered**: Uses Google Gemini Vision API for multimodal inference
- ⚡ **Fast**: One-shot CLI execution with latency timing
- 🎯 **Decision Mode**: Automatically reduces AI responses to LONG/SHORT signals
- 📝 **Raw Mode**: Get full AI analysis when you need detailed explanations
- 🔒 **Secure**: API keys stored in environment variables, never hardcoded

## Prerequisites

- Python 3.11 or higher
- Google API key for Gemini Vision API
- macOS, Linux, or Windows with terminal access

## Installation

### 1. Install Python 3.11+

Download from [python.org](https://www.python.org/downloads/) or use your system's package manager.

Verify installation:
```bash
python --version
```

### 2. Clone or Download This Project

```bash
cd c113-cli
```

### 3. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate it:
- **macOS/Linux**: `source venv/bin/activate`
- **Windows**: `venv\Scripts\activate`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Your API Key

On Replit, the API key is already configured in Secrets. For local use, create a `.env` file in the project root:

```
GOOGLE_API_KEY=AIzaSyBxjSemr-JesFQPfKrLP2FtR8oxsMu4Rdw
```

**Important**: Never commit the `.env` file to version control. It's already in `.gitignore`.

## Usage

### Basic Command Structure

```bash
python c113_cli.py --image <path_to_image> --prompt <your_instruction> [--mode decision|raw]
```

### Example: Get a Trading Decision

```bash
python c113_cli.py \
  --image ./screenshots/option_chain.png \
  --prompt "Read this screenshot and tell me ONLY LONG or SHORT. Say just one word." \
  --mode decision
```

**Output:**
```
LONG
[latency 1.82s]
```

The decision (`LONG` or `SHORT`) is printed to stdout, and the latency timing is printed to stderr.

### Example: Get Full AI Analysis

```bash
python c113_cli.py \
  --image ./screenshots/option_chain.png \
  --prompt "Analyze this option chain and explain your recommendation." \
  --mode raw
```

**Output:**
```
Based on the option chain data, I see significant call volume at the 450 strike with 
increasing open interest. The put/call ratio suggests bullish sentiment. I recommend 
going LONG on this position.
[latency 2.14s]
```

## Command-Line Arguments

| Argument | Required | Description | Default |
|----------|----------|-------------|---------|
| `--image` | Yes | Path to the screenshot/image file | - |
| `--prompt` | Yes | Your instruction for the AI model | - |
| `--mode` | No | Output mode: `decision` or `raw` | `decision` |

### Output Modes

- **decision**: Extracts LONG/SHORT signal from AI response (ideal for automated trading)
- **raw**: Returns the full AI analysis (useful for detailed insights)

## Piping Output to Trading Scripts

Since the decision is printed to stdout, you can easily pipe it to your trading executor:

```bash
DECISION=$(python c113_cli.py --image ./snap.png --prompt "LONG or SHORT?" --mode decision)
echo "Executing trade: $DECISION"
./trade_executor.sh $DECISION
```

## File Structure

```
c113-cli/
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── .env               # API key (not committed to git)
├── .gitignore         # Prevents .env from being committed
├── config.py          # Environment variable loader
├── utils.py           # Image encoding and response parsing
├── ai_client.py       # Gemini API client
└── c113_cli.py        # Main CLI entrypoint
```

## How It Works

1. **Image Encoding**: Your screenshot is base64-encoded with automatic MIME type detection
2. **API Call**: The image and prompt are sent to Google Gemini Vision API
3. **Response Processing**: The AI's response is parsed and optionally reduced to a decision
4. **Output**: Clean output to stdout (for piping) with timing to stderr (for monitoring)

## Troubleshooting

### "Error: GOOGLE_API_KEY not found in environment"

Make sure you've created the `.env` file with your API key, or on Replit, ensure the secret is added.

### "Image file not found"

Check that the path to your image is correct. Use relative or absolute paths.

### "API call failed with status 400"

- Verify your API key is valid
- Check that the image format is supported (PNG, JPEG)
- Ensure the image file isn't corrupted

### "API call failed with status 403"

Your API key may not have access to the Gemini Vision API. Check your Google Cloud project permissions.

## Performance Tips

- Keep image file sizes reasonable (under 5MB)
- Use PNG or JPEG formats
- The `--mode decision` is faster than `--mode raw` for parsing

## Security Notes

- Never commit your `.env` file
- Never share your API key publicly
- On Replit, use Secrets to store the API key securely
- The tool never prints your API key to the console

## License

This tool is provided as-is for personal and educational use.
