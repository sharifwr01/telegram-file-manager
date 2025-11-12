"""
Configuration Template for Telegram File Manager Bot

INSTRUCTIONS:
1. Copy this file to 'config.py'
2. Fill in your credentials
3. Never commit config.py to Git (it's in .gitignore)
"""

# Get these from https://my.telegram.org
API_ID = 12345678  # Your API ID (number)
API_HASH = "your_api_hash_here"  # Your API Hash (string)

# Get this from @BotFather on Telegram
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # Your Bot Token

# Get this from @userinfobot on Telegram
ALLOWED_USER_ID = 123456789  # Your Telegram User ID

# Set your storage path
# Examples:
# - Android (Termux): "/sdcard" or "/storage/emulated/0"
# - Linux: "/home/username" or "/home/username/Documents"
# - Windows: "C:\\Users\\YourName" or "D:\\"
# - macOS: "/Users/username" or "/Users/username/Documents"
BASE_PATH = "/sdcard"

# Optional: Customize these settings
ITEMS_PER_PAGE = 12  # Number of items to show per page
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2GB in bytes
