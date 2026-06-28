# EMV Simulator

## Project Overview

The EMV Simulator is a small Python-based emulator and utilities for experimenting with EMV (Europay, MasterCard, and Visa) transaction flows, TLV parsing, APDU command scaffolding, and basic cryptographic helpers. This branch adds a minimal Flask-based web UI and JSON API to drive the simulator in a browser or via HTTP clients.

## Requirements

- Python 3.8+
- Install dependencies from requirements.txt

## Installation

```bash
git clone https://github.com/DuvalC904/EMV-sim.git
cd EMV-sim
python -m pip install -r requirements.txt
```

## Run the Flask demo app

Start the development server:

```bash
python web_app.py
```

The app will be available at http://127.0.0.1:5000/ — open that URL in your browser to use the tiny UI.

## API endpoints

- GET  /api/status — health and current transaction flow
- POST /api/transaction/initiate  { "amount": <number> }
- POST /api/transaction/process
- POST /api/transaction/complete
- GET  /api/transaction/flow
- POST /api/example { "amount": <number>, "merchant_id": "..." } — run the example transaction flow (authorization randomly approves or declines)

Example curl usage:

```bash
# initiate a transaction for 100.00
curl -X POST -H "Content-Type: application/json" -d '{"amount":100.0}' http://127.0.0.1:5000/api/transaction/initiate

# process
curl -X POST http://127.0.0.1:5000/api/transaction/process

# complete
curl -X POST http://127.0.0.1:5000/api/transaction/complete

# get flow
curl http://127.0.0.1:5000/api/transaction/flow

# run example transaction
curl -X POST -H "Content-Type: application/json" -d '{"amount":50.0}' http://127.0.0.1:5000/api/example
```

## Notes

- This server is intended for local development and experimentation only. It uses a single in-memory EMVSimulator instance that persists state while the process is running.
- Flask is already listed in requirements.txt; no additional dependencies are required for the web UI.

## Contributing

If you'd like additional endpoints (reset, persistent storage, multi-session support, authentication, HTTPS), tell me which behavior you prefer and I will extend the API.
