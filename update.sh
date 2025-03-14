#!/bin/bash
git pull origin main  # Pull the latest changes from GitHub
pkill -f bot.py       # Stop the bot
nohup python3 bot.py &  # Restart the bot in the background
