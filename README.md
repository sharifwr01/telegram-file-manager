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

Edit `bot.py` and replace the placeholder values:

```python
API_ID = 12345678  # Your API ID from my.telegram.org
API_HASH = "your_api_hash_here"  # Your API Hash
BOT_TOKEN = "your_bot_token_here"  # Your Bot Token from @BotFather
ALLOWED_USER_ID = 123456789  # Your Telegram User ID
BASE_PATH = "/sdcard"  # Your storage path (see below)
```

#### Base Path Examples:

- **Android (Termux):** `/sdcard` or `/storage/emulated/0`
- **Linux:** `/home/username` or `/home/username/Documents`
- **Windows:** `C:\\Users\\YourName` or `D:\\`
- **macOS:** `/Users/username` or `/Users/username/Documents`

### 5. Run the Bot

```bash
python bot.py
```

You should see:

```
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

### 6. Use the Bot

1. Open your bot in Telegram
2. Send `/start`
3. Send `/browse` to start browsing files
4. Click folders to navigate
5. Click files to download

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

## ⚙️ Configuration Options

You can customize the bot behavior by editing these variables in `bot.py`:

```python
ITEMS_PER_PAGE = 12  # Number of items to show per page (default: 12)
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # Maximum file size (default: 2GB)
```

### Allow Multiple Users

To allow multiple users to access the bot:

```python
# Replace single user ID
ALLOWED_USER_IDS = [123456789, 987654321, 555555555]

# Update check_access function
def check_access(user_id):
    return user_id in ALLOWED_USER_IDS
```

---

## 🔧 Troubleshooting

### Problem: "API credentials not configured"

**Solution:** Make sure you've replaced all placeholder values in the configuration:
- `API_ID` must be a number
- `API_HASH` must be a string
- `BOT_TOKEN` must be your actual bot token
- `ALLOWED_USER_ID` must be your Telegram user ID

### Problem: "Path not found"

**Solution:** Check your `BASE_PATH` setting. Make sure:
- The path exists on your system
- You have read permissions for that directory
- On Android/Termux, run `termux-setup-storage` first

### Problem: "Access denied to this folder"

**Solution:** 
- Some system folders are protected
- On Android, grant storage permissions to Termux
- Try a different base path that you have access to

### Problem: Session file error

**Solution:** Delete the session file and restart:
```bash
rm file_manager_bot.session
python bot.py
```

### Problem: Slow upload speed

**Solution:**
- Install TgCrypto for faster encryption: `pip install tgcrypto`
- Use a stable internet connection
- Avoid using VPN if possible

### Problem: "Upload failed"

**Solution:**
- Check your internet connection
- Verify the file isn't corrupted
- Make sure file size is under 2GB
- Try uploading a smaller file first

---

## 🌟 Advanced Usage

### Run in Background (Linux/Termux)

Using `screen`:

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

Using `tmux`:

```bash
# Install tmux
pkg install tmux  # Termux

# Start tmux session
tmux new -s filebot

# Run the bot
python bot.py

# Detach: Press Ctrl+B then D
# Reattach later: tmux attach -t filebot
```

### Auto-restart on Crash

Create a wrapper script `run.sh`:

```bash
#!/bin/bash
while true; do
    python bot.py
    echo "Bot crashed! Restarting in 5 seconds..."
    sleep 5
done
```

Make it executable and run:

```bash
chmod +x run.sh
./run.sh
```

### Run as System Service (Linux)

Create `/etc/systemd/system/filebot.service`:

```ini
[Unit]
Description=Telegram File Manager Bot
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/telegram-file-manager
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable filebot
sudo systemctl start filebot
sudo systemctl status filebot
```

---

## 📊 Performance Tips

1. **Install TgCrypto** for 10x faster encryption:
   ```bash
   pip install tgcrypto
   ```

2. **Reduce items per page** if you have limited RAM:
   ```python
   ITEMS_PER_PAGE = 8
   ```

3. **Use SSD storage** for faster file reading

4. **Close other apps** when uploading large files

5. **Use Ethernet/WiFi** instead of mobile data for better speeds

---

## 🔒 Security Best Practices

### Protect Your Credentials

1. **Never commit credentials** to Git:

   Create a `.gitignore` file:
   ```
   *.session
   config.py
   __pycache__/
   *.pyc
   ```

2. **Use environment variables** (recommended):

   ```python
   import os
   
   API_ID = int(os.getenv("API_ID"))
   API_HASH = os.getenv("API_HASH")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID"))
   ```

   Then set them:
   ```bash
   export API_ID=12345678
   export API_HASH="your_api_hash"
   export BOT_TOKEN="your_token"
   export ALLOWED_USER_ID=123456789
   ```

3. **Use a config file** (alternative):

   Create `config.py`:
   ```python
   API_ID = 12345678
   API_HASH = "your_api_hash"
   BOT_TOKEN = "your_token"
   ALLOWED_USER_ID = 123456789
   BASE_PATH = "/sdcard"
   ```

   In `bot.py`:
   ```python
   from config import API_ID, API_HASH, BOT_TOKEN, ALLOWED_USER_ID, BASE_PATH
   ```

   Add `config.py` to `.gitignore`

### Session File Security

- The `.session` file contains your authentication
- **Never share** this file with anyone
- Keep it in a secure location
- Add `*.session` to `.gitignore`

---

## 🐛 Known Issues

1. **File size limit:** Maximum 2GB per file (Telegram limitation)
2. **Hidden files:** Files starting with `.` are automatically hidden
3. **Special characters:** Some filenames with special characters may cause issues
4. **Symlinks:** Symbolic links are treated as regular files/folders

---

## 📚 FAQ

**Q: Why 2GB and not more?**  
A: Telegram's maximum file size is 2GB for regular users (4GB for Premium users).

**Q: Can I use this bot for multiple users?**  
A: Yes, see the "Allow Multiple Users" section in Configuration Options.

**Q: Is the session file safe?**  
A: Yes, but keep it private. It contains your authentication tokens.

**Q: Does this work on iOS?**  
A: You need a jailbroken device to run Python on iOS. Consider using Pythonista app.

**Q: Can I host this on a server?**  
A: Yes! You can host it on any server with Python 3.8+ installed.

**Q: Why do I need API credentials?**  
A: To support 2GB files, we use Telegram's Client API instead of Bot API.

**Q: Will my files be uploaded to Telegram servers?**  
A: Yes, that's how Telegram works. Files are encrypted and stored on Telegram's servers.

**Q: Can I delete files through the bot?**  
A: Currently, no. This bot is read-only for safety. File deletion may be added in future versions.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/improvement`)
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** your changes (`git commit -am 'Add new feature'`)
6. **Push** to the branch (`git push origin feature/improvement`)
7. **Create** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/telegram-file-manager.git
cd telegram-file-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

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

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐️ on GitHub!

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

### v1.0.0
- Initial release
- Basic file browsing
- 50MB file limit (Bot API)
- Simple navigation

---

<p align="center">
  <b>Made with ❤️ by developers, for developers</b>
</p>

<p align="center">
  <a href="#-telegram-file-manager-bot">Back to Top ⬆️</a>
</p>
