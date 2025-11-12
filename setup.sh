#!/bin/bash

# Telegram File Manager Bot - Quick Setup Script
# This script helps you set up the bot quickly

echo "======================================================================"
echo "🤖 Telegram File Manager Bot - Quick Setup"
echo "======================================================================"
echo ""

# Check if Python is installed
echo "📋 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8 or higher from https://www.python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "⚠️  Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Create config file if it doesn't exist
if [ ! -f "config.py" ]; then
    echo "📝 Creating configuration file..."
    cp config.example.py config.py
    echo "✅ config.py created"
    echo ""
    echo "======================================================================"
    echo "⚠️  IMPORTANT: You need to configure the bot!"
    echo "======================================================================"
    echo ""
    echo "Edit config.py and add your credentials:"
    echo ""
    echo "1. API_ID and API_HASH from https://my.telegram.org"
    echo "2. BOT_TOKEN from @BotFather on Telegram"
    echo "3. ALLOWED_USER_ID from @userinfobot on Telegram"
    echo "4. BASE_PATH (your storage path)"
    echo ""
    echo "After configuration, run: python bot.py"
    echo ""
else
    echo "⚠️  config.py already exists"
    echo ""
    echo "======================================================================"
    echo "✅ Setup Complete!"
    echo "======================================================================"
    echo ""
    echo "To start the bot, run:"
    echo "  source venv/bin/activate"
    echo "  python bot.py"
    echo ""
fi

echo "======================================================================"
echo "📚 Need help? Check the README.md file"
echo "======================================================================"
