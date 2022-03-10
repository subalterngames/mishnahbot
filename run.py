from argparse import ArgumentParser
from mishnabot.bot import Bot

"""
Run the bot.

Usage:

```
python3 run.py --token TOKEN --channel CHANNEL
```
"""

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--token")
    parser.add_argument("--channel")
    args = parser.parse_args()
    bot = Bot(channel=args.channel)
    bot.run(args.token)
