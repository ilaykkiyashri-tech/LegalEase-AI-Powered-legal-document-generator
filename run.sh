#!/bin/bash
# Starts the FastAPI backend and Streamlit frontend together.
set -e

source venv/bin/activate 2>/dev/null || true

uvicorn legalEaseAPI.main:app --reload --port 8000 &
BACKEND_PID=$!

sleep 2
streamlit run frontend/app.py

kill $BACKEND_PID
