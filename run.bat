@echo off
title Regulatory Compliance AI Agent
color 0B

REM Activate virtual environment
IF NOT EXIST venv\Scripts\activate.bat (
    echo [ERROR] Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

REM Check .env has a real API key
IF NOT EXIST .env (
    echo [ERROR] .env file not found. Please run setup.bat first.
    pause
    exit /b 1
)

findstr /C:"your_api_key_here" .env >nul 2>&1
IF NOT ERRORLEVEL 1 (
    echo [ERROR] API key not set. Please edit .env and replace "your_api_key_here"
    echo         with your real Anthropic API key from https://console.anthropic.com
    pause
    exit /b 1
)

REM Parse optional arguments and launch
IF "%1"=="" (
    REM Interactive mode
    python main.py
) ELSE (
    REM Pass all arguments through (e.g. --company "Emaar" --region UAE)
    python main.py %*
)

pause
