# Alpaca Paper Trading CLI

## Overview
A minimal Python command-line trading tool for instant paper trading on Alpaca. This tool allows ultra-fast order execution - simply type `long` or `short` and press Enter to submit market orders in under 1 second.

**Current State:** Fully functional and ready to use. The trading CLI is configured with Alpaca paper trading credentials and can execute instant trades.

## Recent Changes
- **2025-10-28:** Initial project setup complete
  - Created config.py with Alpaca API credentials
  - Implemented broker.py with go_long() and go_short() functions
  - Built main.py with instant command loop (no confirmations)
  - Configured workflow to run the trading CLI
  - Installed Python 3.11 and requests library

## Project Architecture

### File Structure
```
.
├── config.py          # Alpaca API credentials
├── broker.py          # Trading functions (go_long, go_short)
├── main.py            # Command loop interface
├── requirements.txt   # Python dependencies
└── README.md          # User documentation
```

### Key Components

**config.py**
- Stores Alpaca paper trading API credentials
- Contains API key, secret key, and base URL

**broker.py**
- Default symbol: SPY (configurable at top of file)
- Default quantity: 1 share (configurable at top of file)
- `go_long()`: Submits market BUY order
- `go_short()`: Submits market SELL SHORT order
- Error handling for HTTP failures and order rejections

**main.py**
- Infinite input loop for instant command execution
- Commands: `long` (buy), `short` (sell)
- Displays order ID and status after each trade
- Continues running after errors (non-crashing)

### API Integration
- Uses Alpaca Paper Trading API v2
- Endpoint: https://paper-api.alpaca.markets/v2/orders
- Authentication via APCA-API-KEY-ID and APCA-API-SECRET-KEY headers
- Order type: Market orders with DAY time-in-force

## Usage
The Trading CLI workflow is running. Type `long` or `short` in the console to execute trades instantly.

## Dependencies
- Python 3.11
- requests==2.31.0
