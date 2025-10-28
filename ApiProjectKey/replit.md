# c113-cli: AI Trading Decision Tool

## Project Overview
A command-line tool that analyzes trading screenshots (option chains, tape data, etc.) using Google Gemini Vision API to generate instant LONG/SHORT trading decisions. Designed for terminal-based trading workflows where decisions can be piped directly to trading executors.

## Purpose
Enable fast, AI-powered trading decision-making without web UIs or browser interactions. Users provide a screenshot and a prompt, and the tool outputs a clean trading signal.

## Current State
- ✅ Fully functional CLI application
- ✅ Google Gemini 2.5 Flash Vision API integration
- ✅ Secure API key management via environment variables
- ✅ Dual output modes: decision (LONG/SHORT) and raw (full analysis)
- ✅ Performance timing (latency tracking)
- ✅ Tested and verified working

## Recent Changes
**2025-10-28**: Initial implementation
- Created modular CLI structure (config, utils, ai_client, main CLI)
- Integrated Google Gemini Vision API with gemini-2.5-flash model
- Implemented base64 image encoding with MIME type detection
- Added decision extraction logic for LONG/SHORT signals
- Set up secure API key management using Replit Secrets
- Verified working with test images

## Project Architecture

### File Structure
```
c113-cli/
├── c113_cli.py      # Main CLI entrypoint (argparse, orchestration)
├── ai_client.py     # Gemini API client (HTTP calls)
├── config.py        # Environment variable loader
├── utils.py         # Image encoding, response parsing, decision extraction
├── requirements.txt # Python dependencies
├── README.md        # User documentation
└── .gitignore       # Prevents committing .env files
```

### Key Components
1. **config.py**: Loads GOOGLE_API_KEY from environment, exits cleanly if missing
2. **utils.py**: 
   - `encode_image_to_base64()`: PNG/JPEG encoding with MIME detection
   - `extract_text_from_response()`: Defensive JSON parsing
   - `reduce_to_decision()`: Extracts LONG/SHORT from AI text
3. **ai_client.py**: Calls Gemini v1beta endpoint with multimodal content
4. **c113_cli.py**: Argparse CLI, timing, stdout/stderr handling

### API Integration
- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent`
- **Authentication**: API key via query parameter
- **Request**: Multimodal (text prompt + base64 inline image)
- **Response**: JSON with `candidates[0].content.parts[0].text`

## Usage Pattern
This is a **one-shot CLI tool**, not a continuous service. Users run it on-demand:

```bash
python c113_cli.py \
  --image ./screenshots/option_chain.png \
  --prompt "LONG or SHORT?" \
  --mode decision
```

Output (to stdout): `LONG`  
Timing (to stderr): `[latency 4.21s]`

## User Preferences
- **No web UI**: Terminal-only interaction
- **Pipeable output**: Clean stdout for integration with trading scripts
- **Fast execution**: Latency timing for performance monitoring
- **Security**: API keys in environment, never logged or exposed

## Dependencies
- Python 3.11+
- requests (HTTP client)
- python-dotenv (environment variables)

## Technical Decisions
1. **Model choice**: gemini-2.5-flash (fast, cost-efficient, good for vision)
2. **No async**: Single synchronous HTTP call per run (simple, reliable)
3. **Error handling**: Explicit RuntimeError for HTTP failures, FileNotFoundError for missing images
4. **Output separation**: Decision to stdout, timing/errors to stderr (enables piping)
5. **Type hints**: Full typing for maintainability

## Notes
- This is NOT a web server or daemon - it's a command-line utility
- Each execution is independent (no state between runs)
- Designed for integration into larger trading automation workflows
