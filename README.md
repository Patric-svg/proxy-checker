# Proxy Checker

A small Python utility for checking proxy availability and response behavior.

## Features

- Reads proxy candidates from the configured input source.
- Performs concurrent checks to reduce waiting time.
- Reports reachable and unavailable proxies.

## Requirements

- Python 3.10 or newer

## Run locally

```bash
git clone https://github.com/Patric-svg/proxy-checker.git
cd proxy-checker
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
python checker.py
```

Review `checker.py` before running and adapt its input format to your data source.

## Responsible use

Only test proxies and networks that you own or are authorized to assess. Do not use this tool to bypass access controls, evade monitoring, or conduct unauthorized scanning.

## Status

This is an educational utility. Validate behavior and error handling before using it in an operational workflow.
