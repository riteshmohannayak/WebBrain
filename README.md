# WebBrain — AI Web Intelligence Platform

## Overview

WebBrain is a full-stack GenAI system that scrapes, summarizes, and semantically analyzes websites using local LLMs via Ollama.

## Quick Start

1. Make sure you have Docker and Docker Compose installed.
2. Run:
   ```bash
   cd infra
   docker compose up --build
   ```

# Tech Stack That I have Used

- Backend — FastAPI app (Python)
- Worker — Celery worker for async scraping/summarization
- Redis — message queue
- Postgres — main database
- ChromaDB — vector database
- Nginx — reverse proxy
