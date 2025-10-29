# Alpaca Paper Trading CLI

A minimal command-line trading tool for instant paper trading on Alpaca. Type `long` or `short` and execute market orders in under 1 second.

## Setup Instructions

### Step 1: Install Python 3
Make sure you have Python 3 installed on your system. You can check by running:
```bash
python3 --version
```

If you don't have Python 3, download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies
Open your terminal in this project folder and run:
```bash
pip install -r requirements.txt
```

### Step 3: Configure Your API Keys
Edit `config.py` and replace the placeholder values with your Alpaca paper trading credentials:

```python
ALPACA_API_KEY = "YOUR_API_KEY_HERE"
ALPACA_SECRET_KEY = "YOUR_SECRET_KEY_HERE"
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"
```

**Important:** Make sure you're using PAPER trading credentials, not live trading keys.

### Step 4: Run the Trading Tool
Start the trading CLI:
```bash
python3 main.py
```

### Step 5: Execute Trades
Once the program is running, simply type commands and press Enter:

- Type `long` and press Enter to submit a market BUY order
- Type `short` and press Enter to submit a market SELL SHORT order

After each order, you'll see the order ID and status (e.g., `submitted`, `filled`).

The program will keep running and listening for more commands. Press `Ctrl+C` to exit.

## Configuration

You can change the default symbol and quantity by editing the top of `broker.py`:

```python
SYMBOL = "SPY"   # Change to any ticker symbol
QTY = 1          # Change to desired quantity
```

## Commands

- `long` - Submit a market BUY order
- `short` - Submit a market SELL SHORT order
- Any other input will display "unknown command"

## Notes

- This tool is designed for speed. No confirmations, no menus.
- All orders are DAY orders that expire at market close.
- Errors (like insufficient buying power) will be displayed but won't crash the program.
- This is for PAPER trading only. Never use live trading credentials.
