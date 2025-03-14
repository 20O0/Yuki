import os
import telebot
import openai
import requests
import subprocess
import random
import time

# Load tokens from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# Store bot owner ID (replace with your Telegram ID)
BOT_OWNER_ID = 123456789  

# Function to get AI-generated responses
def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Handle commands from bot owner (Works Everywhere)
@bot.message_handler(func=lambda msg: msg.from_user.id == BOT_OWNER_ID)
def handle_bot_owner_commands(message):
    command = message.text.lower()
    if command == "/auto_update":
        bot.send_message(message.chat.id, "Checking for updates...")
        auto_create_update()  # Trigger the automatic update process
    else:
        bot.send_message(message.chat.id, "Unknown command.")

# Auto-create and apply updates
def auto_create_update():
    update_type = random.choice(['group_security', 'font_update', 'feature_update'])

    if update_type == 'group_security':
        apply_group_security_update()
    elif update_type == 'font_update':
        apply_font_update()
    elif update_type == 'feature_update':
        apply_feature_update()

# Example: Applying group security update (e.g., banning users, enabling filters)
def apply_group_security_update():
    bot.send_message(BOT_OWNER_ID, "Security features applied.")
    # Implement security updates, e.g., blocking certain words, banning users, etc.

# Example: Changing font name or applying design update
def apply_font_update():
    bot.send_message(BOT_OWNER_ID, "Font name changed.")
    # Implement logic to change font or related design updates

# Example: Adding a new feature (could be a command or functionality)
def apply_feature_update():
    bot.send_message(BOT_OWNER_ID, "New feature added.")
    # Implement new feature, e.g., adding a new command or functionality

# AI-powered chat (for everyone)
@bot.message_handler(func=lambda msg: True)
def ai_chat(message):
    response = get_ai_response(message.text)
    bot.send_message(message.chat.id, response)

# Function to pull latest code from GitHub and apply updates automatically
def pull_latest_code():
    subprocess.run(["git", "pull", "origin", "main"])  # Pull the latest code from GitHub
    bot.send_message(BOT_OWNER_ID, "Pulled the latest code from GitHub.")

# Polling and running the bot
bot.polling()
  
