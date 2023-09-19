#!/bin/sh

# Start the FastAPI server in the background
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &

# Run the tests in the foreground
pytest ./tests/test_main.py

# Wait indefinitely to keep the container running
trap "echo Stopping...; kill -SIGTERM $!; exit 0" SIGINT SIGTERM
wait
