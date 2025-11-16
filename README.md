# 🎮 UNO Telegram Bot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](./LICENSE)
[![Python 3.4+](https://img.shields.io/badge/python-3.4+-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://telegram.me/unobot)

A powerful Telegram bot that brings the classic UNO card game to your chats! Play UNO with friends directly in Telegram using inline queries.

## 🌟 Features

- **🎯 Inline Gameplay**: Play directly in any chat using inline queries
- **👥 Multiplayer Support**: Play with 2+ players in groups or private chats
- **🎨 Multiple Game Modes**: 
  - **Classic**: Traditional UNO rules
  - **Fast**: Quick-paced games with shorter turn times
  - **Wild**: Chaos mode with special rules
- **🌍 Multi-language Support**: Available in 15+ languages
- **⚙️ Customizable Settings**: Configure turn times, player limits, and default game modes
- **🎴 Beautiful Card Graphics**: High-quality card images including colorblind-friendly versions
- **📊 Game Statistics**: Track your wins and gameplay

## 🚀 Quick Start

### Prerequisites

- Python 3.4 or higher
- pip (Python package manager)
- A Telegram Bot Token from [@BotFather](https://telegram.me/BotFather)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/uno-telegram-bot.git
   cd uno-telegram-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   *Recommended: Use a virtual environment*
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   - Copy `config.json.example` to `config.json`
   ```bash
   cp config.json.example config.json
   ```
   - Edit `config.json` with your settings:
     - `token`: Your bot token from BotFather
     - `admin_list`: List of admin user IDs
     - `default_gamemode`: "classic", "fast", or "wild"
     - `min_players`: Minimum players required (default: 2)
     - `waiting_time`: Time to wait for players to join (seconds)

4. **Compile language files**
   ```bash
   cd locales
   bash compile.sh
   ```
   
   *Alternative (if bash is not available):*
   ```bash
   find . -maxdepth 2 -type d -name 'LC_MESSAGES' -exec bash -c 'msgfmt {}/unobot.po -o {}/unobot.mo' \;
   ```

5. **Set up your bot with BotFather**
   - Use `/setinline` to enable inline mode
   - Use `/setinlinefeedback` to enable feedback
   - Use `/setcommands` and paste the contents of `commandlist.txt`

6. **Run the bot**
   ```bash
   python3 bot.py
   ```
   
   *Or use the start script:*
   ```bash
   python3 start_bot.py
   ```

## 📋 Configuration Options

Edit `config.json` to customize your bot:

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| `token` | string | Your Telegram bot token | Required |
| `admin_list` | array | List of admin user IDs | `[0]` |
| `open_lobby` | boolean | Allow anyone to join games | `true` |
| `enable_translations` | boolean | Enable multi-language support | `false` |
| `workers` | integer | Number of worker threads | `32` |
| `default_gamemode` | string | Default game mode (classic/fast/wild) | `"fast"` |
| `waiting_time` | integer | Seconds to wait for players | `120` |
| `time_removal_after_skip` | integer | Time reduction after skip | `20` |
| `min_fast_turn_time` | integer | Minimum turn time in fast mode | `15` |
| `min_players` | integer | Minimum players to start | `2` |

## 🎮 How to Play

1. **Start a game**: Type `@yourbotname` in any chat
2. **Create a game**: Select "Create game" from inline results
3. **Join game**: Other players click "Join game"
4. **Start**: When ready, click "Start game"
5. **Play**: Click on your cards to play them, follow UNO rules!

### Game Commands

- `/new` - Create a new game
- `/join` - Join an existing game
- `/leave` - Leave the current game
- `/open` - Open the lobby to everyone
- `/close` - Restrict lobby to current players
- `/enable_translations` - Enable translations
- `/disable_translations` - Disable translations
- `/skip` - Vote to skip a player's turn
- `/notify_me` - Enable turn notifications
- `/stats` - View your game statistics
- `/modes` - View available game modes
- `/help` - Display help information

## 🐳 Docker Deployment

Run the bot using Docker:

```bash
docker-compose up -d
```

Or build manually:

```bash
docker build -t uno-bot .
docker run -d --name uno-bot -v $(pwd)/config.json:/app/config.json uno-bot
```

## 🛠️ Project Structure

```
.
├── bot.py                 # Main bot file
├── game.py               # Game logic
├── player.py             # Player management
├── card.py               # Card definitions
├── deck.py               # Deck management
├── game_manager.py       # Game state management
├── actions.py            # Game actions
├── results.py            # Inline query results
├── config.py             # Configuration loader
├── database.py           # Database operations
├── settings.py           # User settings
├── internationalization.py # Translation support
├── locales/              # Translation files
├── images/               # Card images and assets
└── chart/                # Kubernetes deployment charts
```

## 🌍 Supported Languages

- 🇨🇦 Catalan (ca_CA)
- 🇩🇪 German (de_DE)
- 🇪🇸 Spanish (es_ES)
- 🇮🇳 Hindi (hn_IN)
- 🇮🇩 Indonesian (id_ID)
- 🇮🇹 Italian (it_IT)
- 🇮🇳 Malayalam (ml_IN)
- 🇧🇷 Portuguese (pt_BR)
- 🇷🇺 Russian (ru_RU)
- 🇹🇷 Turkish (tr_TR)
- 🇺🇿 Uzbek (uz_UZ)
- 🇻🇳 Vietnamese (vi_VN)
- 🇨🇳 Chinese Simplified (zh_CN)
- 🇭🇰 Chinese Hong Kong (zh_HK)
- 🇹🇼 Chinese Traditional (zh_TW)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Adding Translations

To add a new language:
1. Create a new folder in `locales/` (e.g., `locales/fr_FR/LC_MESSAGES/`)
2. Copy `locales/unobot.pot` to your new folder as `unobot.po`
3. Translate the strings in `unobot.po`
4. Run the compile script to generate `.mo` files
5. Add your language code to `locales/available.py`

## 📦 Dependencies

- **python-telegram-bot (13.15)**: Telegram Bot API wrapper
- **Pony ORM (0.7.19)**: Database management

See `requirements.txt` for full dependency list.

## 📝 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Credits

**Original Author**: [Jannes Höke](https://github.com/jh0ker)

### Contributors

Special thanks to all contributors who have helped improve this project:
- [divadsn](https://github.com/divadsn)
- [imlonghao](https://github.com/imlonghao)
- [Iuri Guilherme](https://github.com/iuriguilherme)
- [JuniorJPDJ](https://github.com/JuniorJPDJ)
- [pan93412](https://github.com/pan93412)
- [qubitnerd](https://github.com/qubitnerd)
- [SYHGroup](https://github.com/SYHGroup)

## 🔗 Links

- **Live Bot**: [@unobot](https://telegram.me/unobot)
- **Issues**: [GitHub Issues](https://github.com/yourusername/uno-telegram-bot/issues)
- **Telegram Bot API**: [Documentation](https://core.telegram.org/bots/api)

## 📞 Support

If you have questions or need help:
- Open an [issue](https://github.com/yourusername/uno-telegram-bot/issues)
- Check existing documentation
- Join our community chat (if available)

## ⚠️ Disclaimer

This is an unofficial UNO game implementation. UNO is a trademark of Mattel. This project is not affiliated with or endorsed by Mattel.

---

**Made with ❤️ for the Telegram community**

*Last updated: November 2025*
