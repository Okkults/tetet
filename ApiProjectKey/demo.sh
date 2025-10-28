#!/bin/bash

echo "======================================"
echo "c113-cli Trading Decision Tool Demo"
echo "======================================"
echo ""
echo "This is a command-line tool for AI-powered trading decisions."
echo "Run it on-demand with your own images:"
echo ""
echo "  python c113_cli.py --image <path> --prompt <text> --mode decision"
echo ""
echo "Example with test image:"
echo "--------------------------------------"
echo ""

python c113_cli.py \
  --image test_sample.png \
  --prompt "What do you see in this image? If this were an option chain, would you go LONG or SHORT?" \
  --mode raw

echo ""
echo "--------------------------------------"
echo "Done! Use your own trading screenshots for real analysis."
echo ""
echo "For help: python c113_cli.py --help"
