"""
Telegram File Manager Bot
A powerful bot to browse and download files from your device storage.
Supports files up to 2GB with real-time progress tracking.

Author: Shariful Islam Shakib
License: MIT
Repository: https://github.com/sharifwr01/telegram-file-manager
"""

import os
import hashlib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
import mimetypes
from pathlib import Path

# ========== CONFIGURATION ==========
# Two ways to configure:
# 1. Create config.py file (recommended for GitHub)
# 2. Set values directly here (if not using GitHub)

try:
    # Try to import from config.py
    from config import API_ID, API_HASH, BOT_TOKEN, ALLOWED_USER_ID, BASE_PATH
    print("✅ Configuration loaded from config.py")
except ImportError:
    # Fallback: Use direct values
    print("⚠️  config.py not found. Using values from bot.py")
    print("💡 For better security, create config.py (see config.example.py)")
    
    # Get these from:
    # - API_ID & API_HASH: https://my.telegram.org
    # - BOT_TOKEN: @BotFather on Telegram
    # - ALLOWED_USER_ID: @userinfobot on Telegram
    
    API_ID = 12345678  # Replace with your API ID
    API_HASH = "your_api_hash_here"  # Replace with your API Hash
    BOT_TOKEN = "your_bot_token_here"  # Replace with your Bot Token
    ALLOWED_USER_ID = 123456789  # Replace with your Telegram User ID
    BASE_PATH = "/sdcard"  # Change according to your OS
# ====================================

# Constants
ITEMS_PER_PAGE = 12  # Number of items to show per page
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2GB limit

# Initialize Pyrogram Client
app = Client(
    "file_manager_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Path cache for callback data optimization
path_cache = {}

def get_path_id(path):
    """Generate a short ID for file paths to avoid callback data size limits"""
    path_hash = hashlib.md5(path.encode()).hexdigest()[:12]
    path_cache[path_hash] = path
    return path_hash

def get_path_from_id(path_id):
    """Retrieve original path from short ID"""
    return path_cache.get(path_id, BASE_PATH)

# File type icons mapping
FILE_ICONS = {
    'folder': '📁',
    'image': '🖼',
    'video': '🎥',
    'audio': '🎵',
    'document': '📄',
    'archive': '🗜',
    'apk': '📦',
    'unknown': '📎'
}

def get_file_icon(file_path):
    """Return appropriate icon based on file type"""
    if os.path.isdir(file_path):
        return FILE_ICONS['folder']
    
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        if mime_type.startswith('image'):
            return FILE_ICONS['image']
        elif mime_type.startswith('video'):
            return FILE_ICONS['video']
        elif mime_type.startswith('audio'):
            return FILE_ICONS['audio']
        elif mime_type.startswith('application/pdf') or mime_type.startswith('text'):
            return FILE_ICONS['document']
        elif 'zip' in mime_type or 'rar' in mime_type:
            return FILE_ICONS['archive']
    
    if file_path.endswith('.apk'):
        return FILE_ICONS['apk']
    
    return FILE_ICONS['unknown']

def format_size(size):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def check_access(user_id):
    """Check if user has permission to use the bot"""
    return user_id == ALLOWED_USER_ID

@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    user_id = message.from_user.id
    
    if not check_access(user_id):
        await message.reply_text(
            "❌ **Access Denied!**\n\n"
            f"Your User ID: `{user_id}`\n\n"
            "This bot is private and only authorized users can access it."
        )
        return
    
    await message.reply_text(
        "✅ **File Manager Bot is Running!**\n\n"
        "📱 Use /browse to access your device storage.\n\n"
        "**Available Commands:**\n"
        "• /browse - Browse files and folders\n"
        "• /help - Show help information\n\n"
        "**⚡ Special Feature: Upload files up to 2GB!**"
    )

@app.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    """Handle /help command"""
    if not check_access(message.from_user.id):
        return
    
    await message.reply_text(
        "**📚 File Manager Bot - Help**\n\n"
        "**Commands:**\n"
        "• /start - Start the bot\n"
        "• /browse - Start browsing files\n"
        "• /help - Show this help message\n\n"
        "**Features:**\n"
        "• 📁 Browse folders with beautiful UI\n"
        "• 📄 Download files up to 2GB\n"
        "• 🔄 Pagination support for large directories\n"
        "• 📊 Real-time upload progress bar\n"
        "• 🎨 Smart file type detection\n"
        "• 🔙 Easy navigation (Back/Home buttons)\n\n"
        "**Tips:**\n"
        "• Click folders to navigate inside\n"
        "• Click files to download them\n"
        "• Use Previous/Next buttons for pagination\n"
        "• Hidden files (starting with .) are automatically skipped"
    )

@app.on_message(filters.command("browse") & filters.private)
async def browse_command(client: Client, message: Message):
    """Handle /browse command - start file browsing"""
    if not check_access(message.from_user.id):
        return
    
    await show_directory(client, message, BASE_PATH, page=0)

async def show_directory(client: Client, message: Message, path: str, page: int = 0, is_callback: bool = False):
    """Display directory contents with pagination"""
    try:
        if not os.path.exists(path):
            await message.reply_text("❌ Path not found!")
            return
        
        # Get directory listing
        items = []
        try:
            for item in sorted(os.listdir(path)):
                # Skip hidden files
                if item.startswith('.'):
                    continue
                    
                item_path = os.path.join(path, item)
                try:
                    if os.path.isdir(item_path):
                        items.append(('folder', item, item_path))
                    else:
                        size = os.path.getsize(item_path)
                        items.append(('file', item, item_path, size))
                except (PermissionError, OSError):
                    continue
        except (PermissionError, OSError):
            await message.reply_text("❌ Access denied to this folder!")
            return
        
        if not items:
            await message.reply_text("📭 This folder is empty!")
            return
        
        # Separate folders and files
        folders = [item for item in items if item[0] == 'folder']
        files = [item for item in items if item[0] == 'file']
        
        # Calculate pagination
        total_items = len(folders) + len(files)
        total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
        
        # Validate page bounds
        if page < 0:
            page = 0
        if page >= total_pages:
            page = total_pages - 1
        
        start_idx = page * ITEMS_PER_PAGE
        end_idx = start_idx + ITEMS_PER_PAGE
        
        # Get items for current page
        all_items = folders + files
        page_items = all_items[start_idx:end_idx]
        
        # Build keyboard
        keyboard = []
        
        for item in page_items:
            if item[0] == 'folder':
                icon = get_file_icon(item[2])
                path_id = get_path_id(item[2])
                display_name = item[1]
                if len(display_name) > 30:
                    display_name = display_name[:27] + "..."
                
                keyboard.append([InlineKeyboardButton(
                    f"{icon} {display_name}/",
                    callback_data=f"d:{path_id}:0"
                )])
            else:
                icon = get_file_icon(item[2])
                size_str = format_size(item[3])
                path_id = get_path_id(item[2])
                display_name = item[1]
                if len(display_name) > 25:
                    display_name = display_name[:22] + "..."
                
                keyboard.append([InlineKeyboardButton(
                    f"{icon} {display_name} ({size_str})",
                    callback_data=f"f:{path_id}"
                )])
        
        # Add pagination buttons
        if total_pages > 1:
            page_buttons = []
            
            if page > 0:
                path_id = get_path_id(path)
                page_buttons.append(InlineKeyboardButton(
                    "◀️ Previous",
                    callback_data=f"d:{path_id}:{page-1}"
                ))
            
            page_buttons.append(InlineKeyboardButton(
                f"📄 {page+1}/{total_pages}",
                callback_data="ignore"
            ))
            
            if page < total_pages - 1:
                path_id = get_path_id(path)
                page_buttons.append(InlineKeyboardButton(
                    "Next ▶️",
                    callback_data=f"d:{path_id}:{page+1}"
                ))
            
            keyboard.append(page_buttons)
        
        # Add navigation buttons
        nav_buttons = []
        if path != BASE_PATH:
            parent_path = str(Path(path).parent)
            parent_id = get_path_id(parent_path)
            nav_buttons.append(InlineKeyboardButton("🔙 Back", callback_data=f"d:{parent_id}:0"))
        
        home_id = get_path_id(BASE_PATH)
        nav_buttons.append(InlineKeyboardButton("🏠 Home", callback_data=f"d:{home_id}:0"))
        
        if nav_buttons:
            keyboard.append(nav_buttons)
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Format message text
        current_path = path.replace(BASE_PATH, "") or "/"
        if len(current_path) > 50:
            current_path = "..." + current_path[-47:]
        
        text = f"📂 **Current Path:**\n`{current_path}`\n\n"
        text += f"📊 Total: {len(folders)} folders, {len(files)} files\n"
        
        if total_pages > 1:
            showing_start = start_idx + 1
            showing_end = min(end_idx, total_items)
            text += f"📄 Showing: {showing_start}-{showing_end} (of {total_items})"
        
        # Send or edit message
        if is_callback:
            try:
                await message.edit_text(text, reply_markup=reply_markup)
            except:
                await message.reply_text(text, reply_markup=reply_markup)
        else:
            await message.reply_text(text, reply_markup=reply_markup)
    
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

@app.on_callback_query()
async def callback_handler(client: Client, callback_query: CallbackQuery):
    """Handle button callbacks"""
    if not check_access(callback_query.from_user.id):
        await callback_query.answer("❌ Access denied!", show_alert=True)
        return
    
    data = callback_query.data
    
    if data == "ignore":
        await callback_query.answer()
        return
    
    # Directory navigation
    if data.startswith("d:"):
        await callback_query.answer()
        parts = data.split(":")
        path_id = parts[1]
        page = int(parts[2]) if len(parts) > 2 else 0
        path = get_path_from_id(path_id)
        await show_directory(client, callback_query.message, path, page, is_callback=True)
    
    # File download
    elif data.startswith("f:"):
        await callback_query.answer("📤 Starting file upload...")
        path_id = data[2:]
        file_path = get_path_from_id(path_id)
        await send_file(client, callback_query.message, file_path)

async def send_file(client: Client, message: Message, file_path: str):
    """Send file with progress tracking (supports up to 2GB)"""
    try:
        if not os.path.exists(file_path):
            await message.reply_text("❌ File not found!")
            return
        
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)
        
        # Check file size limit
        if file_size > MAX_FILE_SIZE:
            await message.reply_text(
                f"❌ File too large ({format_size(file_size)})!\n"
                f"Maximum supported size: {format_size(MAX_FILE_SIZE)}"
            )
            return
        
        # Send initial progress message
        progress_msg = await message.reply_text(
            f"📤 **Uploading...**\n\n"
            f"📄 File: `{file_name}`\n"
            f"📊 Size: **{format_size(file_size)}**\n"
            f"⏳ Please wait..."
        )
        
        # Upload file with progress tracking
        try:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            # Progress callback function
            async def progress(current, total):
                try:
                    percentage = (current / total) * 100
                    bar_length = 20
                    filled = int(bar_length * current // total)
                    bar = "█" * filled + "░" * (bar_length - filled)
                    
                    await progress_msg.edit_text(
                        f"📤 **Uploading...**\n\n"
                        f"📄 File: `{file_name}`\n"
                        f"📊 Size: **{format_size(file_size)}**\n\n"
                        f"Progress: `{bar}` {percentage:.1f}%\n"
                        f"Uploaded: {format_size(current)} / {format_size(total)}"
                    )
                except:
                    pass
            
            caption = f"📄 **{file_name}**\n📊 Size: {format_size(file_size)}"
            
            # Send based on file type for better preview
            if mime_type and mime_type.startswith('image'):
                await message.reply_photo(
                    photo=file_path,
                    caption=caption,
                    progress=progress
                )
            elif mime_type and mime_type.startswith('video'):
                await message.reply_video(
                    video=file_path,
                    caption=caption,
                    progress=progress
                )
            elif mime_type and mime_type.startswith('audio'):
                await message.reply_audio(
                    audio=file_path,
                    caption=caption,
                    progress=progress
                )
            else:
                await message.reply_document(
                    document=file_path,
                    caption=caption,
                    progress=progress
                )
            
            # Delete progress message after successful upload
            await progress_msg.delete()
            
        except Exception as e:
            await progress_msg.edit_text(f"❌ Upload failed: {str(e)}")
    
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

def main():
    """Main function to run the bot"""
    print("=" * 70)
    print("🤖 TELEGRAM FILE MANAGER BOT (2GB SUPPORT)")
    print("=" * 70)
    print("📱 Initializing bot...")
    print()
    
    # Validate base path
    if not os.path.exists(BASE_PATH):
        print(f"⚠️  WARNING: Base path '{BASE_PATH}' not found!")
        print("📝 Please configure the correct BASE_PATH")
        print()
    
    # Check configuration
    if API_ID == 12345678 or API_HASH == "your_api_hash_here":
        print("❌ ERROR: API credentials not configured!")
        print("📝 Please configure credentials in config.py or bot.py")
        print("💡 See config.example.py for reference")
        return
    
    if BOT_TOKEN == "your_bot_token_here":
        print("❌ ERROR: BOT_TOKEN not configured!")
        print("📝 Please get your bot token from @BotFather")
        return
    
    print("=" * 70)
    print("✅ BOT STARTED SUCCESSFULLY!")
    print("=" * 70)
    print(f"📁 Base Path: {BASE_PATH}")
    print(f"👤 Allowed User ID: {ALLOWED_USER_ID}")
    print(f"📄 Items per page: {ITEMS_PER_PAGE}")
    print(f"📦 Max file size: {format_size(MAX_FILE_SIZE)}")
    print("=" * 70)
    print("🔄 Bot is now running...")
    print("💡 Press Ctrl+C to stop the bot")
    print("=" * 70)
    print()
    
    # Run the bot
    app.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("=" * 70)
        print("🛑 SHUTTING DOWN BOT...")
        print("=" * 70)
        print("✅ Bot stopped successfully!")
        print("👋 Goodbye!")
        print()
    except Exception as e:
        print()
        print("=" * 70)
        print(f"❌ FATAL ERROR: {e}")
        print("=" * 70)
        print("📝 Please check your configuration and try again")
        print()
