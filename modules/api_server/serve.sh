#!/bin/bash
uvicorn modules.api_server.main:app --reload --port 7744
