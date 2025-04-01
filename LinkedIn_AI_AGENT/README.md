# LinkedIn Tech News Agent

## Overview
Automated tech news posting agent for LinkedIn

## Setup
1. Create virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Set up .env file with credentials
4. Run: `python run.py`

## Features
- Web scraping from multiple tech news sources
- Secure credential management
- Scheduled posting
- Logging and error handling

## Credential Setup

Before running the application, you must set up your credentials:

1. Obtain LinkedIn Developer Credentials:
   - Go to https://www.linkedin.com/developers/
   - Create a new app
   - Get your Client ID and Client Secret

2. Run Credential Setup:
   ```bash
   python setup_credentials.py