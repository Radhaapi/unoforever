# 🎮 ADMIN CHEAT SYSTEM - COMPLETE GUIDE

## 📋 SETUP

### Step 1: Add Your User ID to Config
Edit `config.json` and add your Telegram user ID:
```json
{
    "admin_list": [7876353648, 6504419787]
}
```

**To find your User ID:**
1. Run: `python get_user_id.py`
2. Message your bot with `/start`
3. Bot will reply with your User ID
4. Add it to config.json

---

## 🎯 HOW IT WORKS

### 🔐 All Commands Work in BOT DM ONLY
- **Privacy:** Commands only work in private chat with bot
- **Silent Mode:** Non-admins get no response if they try
- **Cross-Group:** Control games from bot DM even if playing in groups

---

## 🛠️ ALL FEATURES (6 Commands)

### ✅ COMMAND 1: /cheat
**Enable/Disable Cheat Mode**

**Usage:**
```
/cheat    → Toggles cheat mode ON/OFF
```

**What it does:**
- Activates all cheat features
- Must be enabled before using other commands
- Toggle again to disable

**Example:**
```
You: /cheat
Bot: 🎮 Cheat Mode: 🟢 ENABLED
     ✅ All features activated!
```

---

### 👁️ COMMAND 2: /seeall
**See All Players' Cards**

**Usage:**
```
/seeall   → Shows everyone's cards in current game
```

**What it does:**
- Displays all players' cards from your active game
- Shows card count for each player
- Sent privately to you in bot DM

**Example Output:**
```
👁️ ALL CARDS - UNO Game Group

👤 Pratik:
   Red 5, Blue Skip, Wild +4, Green 2
   Total: 4

👤 Rahul:
   Yellow 7, Red Reverse
   Total: 2

👤 Sonia:
   Green Skip, Blue 3, Red 9
   Total: 3
```

**When to use:**
- Plan your strategy
- Know who is close to winning
- See what cards opponents have

---

### 🎴 COMMAND 3: /getcard
**Queue Cards for Next Draw**

**Usage:**
```
/getcard <card>   → Queues card to be added on your next draw
```

**Card Formats:**
- Colors: `red`, `blue`, `green`, `yellow`
- Specials: `skip`, `reverse`, `+2`
- Wilds: `wild`, `wild +4`

**Examples:**
```
/getcard wild +4        → Queue Wild +4
/getcard red skip       → Queue Red Skip
/getcard blue reverse   → Queue Blue Reverse
/getcard green +2       → Queue Green +2
/getcard yellow 7       → Queue Yellow 7
/getcard wild           → Queue Wild (color chooser)
```

**How it works:**
1. Use `/getcard` multiple times to queue cards
2. Cards are stored in a queue
3. Next time you draw in the game → All queued cards are added to your hand!
4. Queue is then cleared

**Example Session:**
```
You: /getcard wild +4
Bot: ✅ Queued: Wild +4
     📋 Queue: 1 cards
     Will be added on your next draw!

You: /getcard wild
Bot: ✅ Queued: Wild
     📋 Queue: 2 cards
     Will be added on your next draw!

[You draw a card in game]
Bot: ✅ Added 2 queued card(s) to your hand!
```

---

### 🔄 COMMAND 4: /replacecard
**Replace Existing Cards**

**Usage:**
```
/replacecard <position> <new_card>
```

**What it does:**
- Instantly replaces a card in your current hand
- Changes happen immediately (not on next draw)
- Use `/mycards` first to see positions

**Examples:**
```
/replacecard 1 wild +4     → Replace card #1 with Wild +4
/replacecard 3 red skip    → Replace card #3 with Red Skip
/replacecard 5 wild        → Replace card #5 with Wild
```

**Complete Example:**
```
You: /mycards
Bot: 🎴 YOUR CARDS - UNO Game
     1. Red 2
     2. Blue 5
     3. Green 7
     Total: 3 cards

You: /replacecard 2 wild +4
Bot: ✅ Replaced!
     Old: Blue 5
     New: Wild +4
```

**When to use:**
- Remove bad cards from your hand
- Get cards you need right now
- Instant advantage without waiting for draw

---

### 🃏 COMMAND 5: /mycards
**View Your Current Cards**

**Usage:**
```
/mycards   → Shows your cards with position numbers
```

**What it does:**
- Lists all your current cards
- Shows position numbers (for /replacecard)
- Displays total count

**Example:**
```
You: /mycards
Bot: 🎴 YOUR CARDS - UNO Game Group
     
     1. Red 5
     2. Blue Skip
     3. Wild +4
     4. Green 2
     5. Yellow Reverse
     
     Total: 5 cards
```

**When to use:**
- Check what you have before replacing
- Find position numbers for /replacecard
- Plan your next move

---

### 📊 COMMAND 6: /cheatstatus
**Check Cheat System Status**

**Usage:**
```
/cheatstatus   → Shows current status and help
```

**What it shows:**
- Cheat mode ON/OFF
- Number of queued cards
- All available commands
- Quick help

**Example:**
```
You: /cheatstatus
Bot: 🎮 CHEAT STATUS
     
     Mode: 🟢 ENABLED
     Queued: 3 cards
     
     Commands (DM only):
     • /cheat - Toggle ON/OFF
     • /seeall - See all cards
     • /getcard - Queue card
     • /replacecard - Replace card
     • /mycards - Your cards
     • /cheatstatus - This status
     
     💡 All commands work in bot DM!
```

---

## 🎮 COMPLETE USAGE EXAMPLE

### Scenario: You want to dominate a game

**Step 1: Enable cheat mode (in bot DM)**
```
You: /cheat
Bot: 🎮 Cheat Mode: 🟢 ENABLED
```

**Step 2: Join a game in group**
```
[In group chat]
You: /new
Bot: Created a new game!

You: /join
Bot: Pratik joined the game

[Others join...]
You: /start
Bot: Game started!
```

**Step 3: Queue powerful cards (in bot DM)**
```
You: /getcard wild +4
Bot: ✅ Queued: Wild +4

You: /getcard wild +4
Bot: ✅ Queued: Wild +4

You: /getcard wild
Bot: ✅ Queued: Wild
     📋 Queue: 3 cards
```

**Step 4: Check opponents (in bot DM)**
```
You: /seeall
Bot: 👁️ ALL CARDS - UNO Group
     
     👤 Rahul: Red 2, Blue 5, Green 7
     👤 Sonia: Yellow Skip, Red 9
     👤 You: Green 3, Blue 2
```

**Step 5: Draw to get queued cards**
```
[In game, when it's your turn]
@unobot → Choose draw option

[In bot DM]
Bot: ✅ Added 3 queued card(s) to your hand!
```

**Step 6: Check your new cards**
```
You: /mycards
Bot: 🎴 YOUR CARDS
     1. Green 3
     2. Blue 2
     3. Wild +4
     4. Wild +4
     5. Wild
     Total: 5 cards
```

**Step 7: Replace bad cards if needed**
```
You: /replacecard 1 red skip
Bot: ✅ Replaced! Old: Green 3, New: Red Skip
```

**Step 8: Dominate the game!**
- Use Wild +4 to punish opponents
- Use Wilds to control color
- Use /seeall to know what others have
- Win easily! 🏆

---

## 🎯 BEST STRATEGIES

### Strategy 1: Silent Winner
```
1. /cheat
2. /getcard wild +4 (multiple times)
3. Play normally
4. Use powerful cards when needed
5. Win without suspicion
```

### Strategy 2: Complete Control
```
1. /cheat
2. /seeall (before each turn)
3. Queue cards that counter opponents
4. Replace bad cards with /replacecard
5. Perfect strategic play
```

### Strategy 3: Quick Domination
```
1. /cheat
2. /getcard wild +4 (5-6 times)
3. /getcard wild (3-4 times)
4. Draw once to get all cards
5. Destroy everyone with Wild +4s
```

### Strategy 4: Stealth Mode
```
1. /cheat
2. Use /seeall to know everyone's cards
3. Don't queue too many cards
4. Play smart using knowledge
5. Win by strategy, not obvious cheating
```

---

## ⚠️ IMPORTANT NOTES

### Privacy & Security
- ✅ All commands work ONLY in bot DM (private chat)
- ✅ Non-admins get NO response (silent ignore)
- ✅ Other players can't see you're using cheats
- ✅ Commands don't show in group chat
- ✅ Only admins in config.json can use

### Limitations
- Must enable `/cheat` first before using other commands
- `/getcard` adds cards on NEXT draw (not instant)
- `/replacecard` changes cards instantly
- Need to be in an active game
- Works across multiple groups

### Tips for Not Getting Caught
1. Don't queue too many cards at once
2. Use `/seeall` sparingly
3. Don't always play perfect moves
4. Mix normal plays with cheat plays
5. Disable `/cheat` when not needed

---

## 📝 QUICK COMMAND REFERENCE

| Command | What it does | When to use |
|---------|-------------|-------------|
| `/cheat` | Toggle ON/OFF | Start of session |
| `/seeall` | See all cards | Before your turn |
| `/getcard <card>` | Queue for draw | Build strong hand |
| `/replacecard <pos> <card>` | Replace now | Need card immediately |
| `/mycards` | View your cards | Check positions |
| `/cheatstatus` | Check status | Verify settings |

---

## 🎪 CARD FORMAT GUIDE

### Colors:
- `red` or `r`
- `blue` or `b`
- `green` or `g`
- `yellow` or `y`

### Numbers:
- `0` to `9`

### Special Cards:
- `skip` - Skip next player
- `reverse` - Reverse direction
- `+2` or `draw` - Draw 2 cards

### Wild Cards:
- `wild` - Color chooser
- `wild +4` - Wild Draw 4

### Examples:
```
red 5          → Red 5
blue skip      → Blue Skip
green reverse  → Green Reverse
yellow +2      → Yellow Draw 2
wild           → Wild (choose color)
wild +4        → Wild Draw 4
```

---

## 🆘 TROUBLESHOOTING

### "⚠️ Enable cheat mode first: /cheat"
→ You need to use `/cheat` to enable before other commands

### "❌ No active game found"
→ Join a game first with `/join` in a group

### "❌ Not in game"
→ You're not a player in the current game

### Commands not working
→ Make sure you're messaging bot in DM (private chat), not group

### Bot not responding
→ Check if your ID is in `admin_list` in config.json

### Cards not adding
→ `/getcard` adds on NEXT draw. Use `/replacecard` for instant

---

## ⚙️ CONFIGURATION

**Current Admin IDs:**
```json
{
    "admin_list": [7876353648, 6504419787]
}
```

**To add more admins:**
1. Get their User ID using `get_user_id.py`
2. Add to config.json
3. Restart bot

---

## 🎊 SUCCESS CHECKLIST

- [ ] Cheat mode enabled with `/cheat`
- [ ] Can see all cards with `/seeall`
- [ ] Successfully queued cards with `/getcard`
- [ ] Cards added after drawing
- [ ] Replaced cards with `/replacecard`
- [ ] Viewed cards with `/mycards`
- [ ] All commands work in bot DM only
- [ ] Won multiple games easily!

---

## 💡 PRO TIPS

1. **Always check `/cheatstatus`** before starting
2. **Use `/seeall` strategically** - don't spam it
3. **Queue cards in batches** - 3-5 at a time
4. **Mix `/getcard` and `/replacecard`** for flexibility
5. **Disable when done** - `/cheat` to turn off
6. **Keep it secret** - Don't tell other players
7. **Use wisely** - Too obvious = suspicious

---

## 🎮 YOU'RE NOW A UNO MASTER!

With these cheat commands, you have complete control over the game!

**Remember:**
- 🔐 All commands in bot DM only
- 🤫 Silent mode for non-admins
- 🎯 Strategic use = Best results
- 🏆 Dominate every game!

**Enjoy your unfair advantage! 🎴**
