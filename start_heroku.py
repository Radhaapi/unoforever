#!/usr/bin/env python3
"""
Heroku startup script - Optimized for quick startup
"""
import os
import sys

def setup_environment():
    """Quick environment check"""
    print("Starting UNO bot on Heroku...")
    print(f"Python version: {sys.version}")
    print(f"Memory available: ~512 MB")
    
    # Check critical environment variables
    token = os.getenv('TOKEN')
    if not token:
        print("ERROR: TOKEN environment variable not set!")
        print("Set it with: heroku config:set TOKEN=your_token_here")
        sys.exit(1)
    
    print(f"TOKEN: {token[:10]}... (configured)")
    print(f"WORKERS: {os.getenv('WORKERS', '32')}")
    print(f"DEFAULT_GAMEMODE: {os.getenv('DEFAULT_GAMEMODE', 'fast')}")
    
    # Disable translations on Heroku to save memory
    if not os.getenv('ENABLE_TRANSLATIONS'):
        os.environ['ENABLE_TRANSLATIONS'] = 'false'
        print("Translations: disabled (saves memory)")
    
    print("\nEnvironment ready! Starting bot...\n")

if __name__ == '__main__':
    setup_environment()
    
    # Import and start the bot
    try:
        import bot
    except Exception as e:
        print(f"\nERROR starting bot: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
