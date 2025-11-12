# 📱 Telegram File Manager Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0+-green.svg)](https://docs.pyrogram.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://telegram.org/)

A powerful Telegram bot that allows you to browse and manage your device storage directly through Telegram. Features beautiful UI, pagination support, and the ability to upload files up to **2GB**!

<p align="center">
  <img src="https://img.shields.io/badge/File_Size-Up_to_2GB-success" alt="2GB Support">
  <img src="https://img.shields.io/badge/Progress-Real--time-brightgreen" alt="Real-time Progress">
  <img src="https://img.shields.io/badge/UI-Beautiful-ff69b4" alt="Beautiful UI">
</p>

---

## ✨ Features

- 📁 **Browse Folders** - Navigate through your device storage with an intuitive interface
- 📄 **Download Files** - Send files up to 2GB directly to Telegram
- 🔄 **Pagination** - Handle large directories with Previous/Next navigation
- 📊 **Progress Bar** - Real-time upload progress tracking
- 🎨 **Smart File Detection** - Automatic file type recognition with icons
- 🖼️ **Media Preview** - Images and videos are sent with proper previews
- 🔒 **Secure Access** - Single user authentication
- ⚡ **Fast Performance** - Optimized with TgCrypto
- 🌐 **Cross-Platform** - Works on Android, Linux, Windows, macOS

---

## 📸 Screenshots

```
📂 Current Path:
/Download

📊 Total: 5 folders, 23 files
📄 Showing: 1-12 (of 28)

📁 Documents/
📁 Pictures/
📁 Videos/
🖼 photo.jpg (2.5 MB)
🎥 video.mp4 (450 MB)
📄 document.pdf (12.3 MB)

[◀️ Previous] [📄 2/3] [Next ▶️]
[🔙 Back] [🏠 Home]
```

---

## 📋 Requirements

- Python 3.8 or higher
- A Telegram account
- Storage access permissions (for mobile devices)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-file-manager.git
cd telegram-file-manager
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get API Credentials

#### A. Get API_ID and API_HASH

1. Visit https://my.telegram.org
2. Log in with your phone number
3. Go to **API Development Tools**
4. Create a new application:
   - **App title:** Any name (e.g., "File Manager")
   - **Short name:** Any short name
   - **Platform:** Choose any (Android recommended)
5. Save your `api_id` and `api_hash`

#### B. Get Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the **Bot Token** provided

#### C. Get Your User ID

1. Open Telegram and search for [@userinfobot](https://t.me/userinfobot)
2. Send `/start`
3. Copy your **User ID**

### 4. Configure the Bot

**Two configuration methods available:**

#### Method A: Using config.py (Recommended for production/GitHub)

1. Copy the example configuration:
```bash
cp config.example.py config.py
```

2. Edit `config.py` with your credentials:
```bash
nano config.py
# or use any text editor
```

3. Fill in your values:
```python
API_ID = 12345678  # Your API ID from my.telegram.org
API_HASH = "your_api_hash_here"  # Your API Hash
BOT_TOKEN = "your_bot_token_here"  # Your Bot Token from @BotFather
ALLOWED_USER_ID = 123456789  # Your Telegram User ID
BASE_PATH = "/sdcard"  # Your storage path
```

**Why use config.py?**
- ✅ Keeps credentials separate from code
- ✅ Safe to push bot.py to GitHub
- ✅ Easier to manage multiple environments
- ✅ Better security practice

#### Method B: Direct configuration in bot.py (For personal use only)

If you're NOT uploading to GitHub, you can edit credentials directly in `bot.py`:

```python
# Find this section in bot.py
API_ID = 12345678  # Replace with your values
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"
ALLOWED_USER_ID = 123456789
BASE_PATH = "/sdcard"
```

⚠️ **Warning:** Do NOT use Method B if you plan to upload to GitHub!

#### Base Path Examples:

- **Android (Termux):** `/sdcard` or `/storage/emulated/0`
- **Linux:** `/home/username` or `/home/username/Documents`
- **Windows:** `C:\\Users\\YourName` or `D:\\`
- **macOS:** `/Users/username` or `/Users/username/Documents`

### 5. Run the Bot

```bash
python bot.py
```

**If using config.py (Method A), you'll see:**
```
✅ Configuration loaded from config.py
======================================================================
🤖 TELEGRAM FILE MANAGER BOT (2GB SUPPORT)
======================================================================
📱 Initializing bot...

======================================================================
✅ BOT STARTED SUCCESSFULLY!
======================================================================
📁 Base Path: /sdcard
👤 Allowed User ID: 123456789
📄 Items per page: 12
📦 Max file size: 2.00 GB
======================================================================
🔄 Bot is now running...
💡 Press Ctrl+C to stop the bot
======================================================================
```

**If config.py not found (Method B), you'll see:**
```
⚠️  config.py not found. Using values from bot.py
💡 For better security, create config.py (see config.example.py)
```

### 6. Use the Bot

1. Open your bot in Telegram
2. Send `/start`
3. Send `/browse` to start browsing files
4. Click folders to navigate
5. Click files to download

---

## 📁 Project Structure

```
telegram-file-manager/
├── bot.py                    # Main bot code
├── config.py                 # Your credentials (create from config.example.py)
├── config.example.py         # Configuration template
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules (prevents uploading credentials)
├── README.md                 # This file
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
└── setup.sh                  # Quick setup script (optional)

# Files that will be auto-generated:
├── file_manager_bot.session  # Telegram session (auto-created on first run)
```

---

## 📝 Configuration Files Explained

### config.example.py
- **Purpose:** Template file showing what configuration is needed
- **Contains:** Example/placeholder values with comments
- **Upload to GitHub:** ✅ YES
- **Edit this file:** ❌ NO (use it as reference only)

### config.py
- **Purpose:** Your actual credentials
- **Contains:** Real API keys, tokens, and settings
- **Upload to GitHub:** ❌ NO (listed in .gitignore)
- **Edit this file:** ✅ YES (add your real values here)

### Why separate files?

```
Without config.py:
bot.py (on GitHub) → Contains your real credentials → ❌ INSECURE!

With config.py:
bot.py (on GitHub) → Imports from config.py → ✅ SECURE!
config.py (local only) → Contains real credentials → ✅ SAFE!
```

---

## 📱 Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and see welcome message |
| `/browse` | Start browsing your device storage |
| `/help` | Show help information and features |

---

## 🎨 File Type Icons

The bot automatically detects file types and displays appropriate icons:

| Icon | File Type | Extensions |
|------|-----------|------------|
| 📁 | Folder | Directories |
| 🖼 | Image | .jpg, .png, .gif, .webp |
| 🎥 | Video | .mp4, .mkv, .avi, .mov |
| 🎵 | Audio | .mp3, .wav, .flac, .m4a |
| 📄 | Document | .pdf, .txt, .doc, .docx |
| 🗜 | Archive | .zip, .rar, .7z, .tar |
| 📦 | APK | .apk |
| 📎 | Other | All other files |

---

## ⚙️ Advanced Configuration

### Customize Bot Behavior

Edit these values in `config.py` (or bot.py):

```python
ITEMS_PER_PAGE = 12  # Items to show per page (default: 12)
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # Max file size (default: 2GB)
```

### Allow Multiple Users

In `config.py`:
```python
# Single user (default)
ALLOWED_USER_ID = 123456789

# Multiple users (modify bot.py)
ALLOWED_USER_IDS = [123456789, 987654321, 555555555]
```

Then in `bot.py`, change:
```python
def check_access(user_id):
    return user_id in ALLOWED_USER_IDS
```

---

## 🔧 Troubleshooting

### Problem: "Configuration not found"

**Solution:**
```bash
# Make sure config.py exists
ls config.py

# If not, create it from example
cp config.example.py config.py

# Then edit config.py with your credentials
nano config.py
```

### Problem: "API credentials not configured"

**Solution:** 
- Check if your `config.py` has real values (not placeholders)
- API_ID should be a number: `12345678` (no quotes)
- API_HASH should be a string: `"abc123..."`
- BOT_TOKEN should be a string: `"1234567890:ABC..."`

### Problem: "ImportError: No module named config"

**Solution:**
```bash
# Make sure config.py is in the same directory as bot.py
ls -la

# Should show:
# bot.py
# config.py
# config.example.py
```

### Problem: "Path not found"

**Solution:** 
- Check your `BASE_PATH` in config.py
- On Android/Termux, run: `termux-setup-storage`
- Verify the path exists: `ls /sdcard` or `cd /sdcard`

### Problem: "Session file error"

**Solution:**
```bash
# Delete session file and restart
rm file_manager_bot.session
python bot.py
```

### Problem: "Access denied to folder"

**Solution:**
- Some system folders are protected
- On Android, grant storage permissions to Termux
- Try a different BASE_PATH

### Problem: Slow upload speed

**Solution:**
```bash
# Install TgCrypto for faster encryption
pip install tgcrypto
```

---

## 🔒 Security Best Practices

### 1. Never Commit Credentials

✅ **GOOD:**
```bash
git add bot.py
git add config.example.py
git add .gitignore
git commit -m "Add bot code"
```

❌ **BAD:**
```bash
git add config.py  # ← NEVER DO THIS!
```

### 2. Verify .gitignore

Before first commit:
```bash
# Check .gitignore contains:
cat .gitignore | grep config.py

# Output should show:
# config.py
```

### 3. Check What Will Be Committed

```bash
# Before git commit, always check:
git status

# Make sure these are NOT listed:
# ❌ config.py
# ❌ *.session

# These SHOULD be listed:
# ✅ bot.py
# ✅ config.example.py
# ✅ .gitignore
```

### 4. Use Environment Variables (Alternative)

For servers or advanced users:

```bash
# Set environment variables
export API_ID=12345678
export API_HASH="your_hash"
export BOT_TOKEN="your_token"
export ALLOWED_USER_ID=123456789

# Run bot
python bot.py
```

Then modify bot.py to use `os.getenv()`.

### 5. Protect Session File

The `.session` file contains your authentication:
- ✅ Keep it private
- ❌ Never share it
- ❌ Never upload to GitHub

---

## 🌟 Advanced Usage

### Run in Background (Linux/Termux)

**Using screen:**
```bash
# Install screen
pkg install screen  # Termux
# or
sudo apt install screen  # Linux

# Start screen session
screen -S filebot

# Run the bot
python bot.py

# Detach: Press Ctrl+A then D
# Reattach later: screen -r filebot
```

**Using tmux:**
```bash
# Install tmux
pkg install tmux

# Start session
tmux new -s filebot

# Run bot
python bot.py

# Detach: Press Ctrl+B then D
# Reattach: tmux attach -t filebot
```

### Auto-restart on Crash

Create `run.sh`:
```bash
#!/bin/bash
while true; do
    python bot.py
    echo "Bot crashed! Restarting in 5 seconds..."
    sleep 5
done
```

Run it:
```bash
chmod +x run.sh
./run.sh
```

### Quick Setup Script

Use the included setup script:
```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Check Python installation
- Create virtual environment
- Install dependencies
- Create config.py from template

---

## 📊 Performance Tips

1. **Install TgCrypto** for 10x faster encryption:
   ```bash
   pip install tgcrypto
   ```

2. **Reduce items per page** if you have limited RAM:
   ```python
   ITEMS_PER_PAGE = 8  # in config.py
   ```

3. **Use SSD storage** for faster file reading

4. **Close other apps** when uploading large files

5. **Use Ethernet/WiFi** instead of mobile data

---

## 🐛 Known Issues

1. **File size limit:** Maximum 2GB per file (Telegram limitation)
2. **Hidden files:** Files starting with `.` are automatically skipped
3. **Special characters:** Some filenames with special characters may cause issues
4. **Symlinks:** Symbolic links are treated as regular files/folders

---

## 📚 FAQ

**Q: Where should I put my credentials?**  
A: In `config.py` (create it from `config.example.py`). Never put real credentials directly in `bot.py` if you're uploading to GitHub.

**Q: What's the difference between config.py and config.example.py?**  
A: 
- `config.example.py` = Template with fake values (upload to GitHub)
- `config.py` = Your real credentials (keep local, never upload)

**Q: I accidentally uploaded config.py to GitHub! What do I do?**  
A: 
1. Immediately revoke your bot token at @BotFather
2. Get new API credentials from my.telegram.org
3. Delete the file from GitHub history
4. Update `.gitignore`

**Q: Why do I need config.py if bot.py has configuration section?**  
A: The bot.py tries to import from config.py first. If not found, it uses values from bot.py. This allows:
- Developers: Use config.py (GitHub safe)
- Personal use: Edit bot.py directly (simpler)

**Q: Can I use environment variables instead?**  
A: Yes! The bot can be modified to use `os.getenv()` for even better security.

**Q: Does config.py work automatically?**  
A: Yes! Just create it, fill your credentials, and run `python bot.py`. The bot automatically imports from it.

**Q: Why 2GB and not more?**  
A: Telegram's maximum file size is 2GB for regular users (4GB for Premium users).

**Q: Can I use this bot for multiple users?**  
A: Yes, see the "Allow Multiple Users" section in Advanced Configuration.

**Q: Will my files be uploaded to Telegram servers?**  
A: Yes, that's how Telegram works. Files are encrypted and stored on Telegram's servers.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test thoroughly
5. Commit (`git commit -am 'Add new feature'`)
6. Push (`git push origin feature/improvement`)
7. Create a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Pyrogram](https://docs.pyrogram.org/) - Telegram MTProto API framework
- [Telegram](https://telegram.org/) - Messaging platform
- All contributors who help improve this project

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/telegram-file-manager/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/telegram-file-manager/discussions)
- **Telegram:** [@yourusername](https://t.me/yourusername)

---

## 📈 Roadmap

- [ ] File/folder deletion support
- [ ] File search functionality
- [ ] Multiple file selection and bulk download
- [ ] File upload from Telegram to device
- [ ] File preview for text files
- [ ] Thumbnail generation for videos
- [ ] Folder compression and download
- [ ] File sharing with expiration links
- [ ] Storage statistics and analysis
- [ ] Custom theme support

---

## 🎯 Version History

### v2.0.0 (Current)
- ✅ Added 2GB file support
- ✅ Real-time progress tracking
- ✅ Smart file type detection
- ✅ Pagination system
- ✅ Improved error handling
- ✅ Better console output
- ✅ Added config.py support
- ✅ Dual configuration method

### v1.0.0
- Initial release
- Basic file browsing
- 50MB file limit (Bot API)
- Simple navigation

---

## 📖 Additional Resources

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Pyrogram Documentation](https://docs.pyrogram.org/)
- [Python Documentation](https://docs.python.org/3/)
- [Git Documentation](https://git-scm.com/doc)

---

<p align="center">
  <b>Made with ❤️ for the Telegram community</b>
</p>

<p align="center">
  <a href="#-telegram-file-manager-bot">Back to Top ⬆️</a>
</p>
