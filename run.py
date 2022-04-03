from argparse import ArgumentParser
from mishnabot.bot import Bot

"""
Run the bot.

Usage:

```
python3 run.py --token TOKEN --channel CHANNEL --shomer --shabbos SHABBOS --logging
```
"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--token", type=str, help="Discord bot token")
    parser.add_argument("--channel", type=int, help="Discord channel ID")
    parser.add_argument("--shomer", action="store_true", help="If added, don't post on Shabbos")
    parser.add_argument("--shabbos", type=int, help="Integer of which day is Shabbos. 1 = Monday.")
    parser.add_argument("--logging", action="store_true", help="If added, enable logging")
    args = parser.parse_args()
    bot = Bot(channel=args.channel, shomer=args.shomer, logging=args.logging, shabbos=args.shabbos)
    bot.run(args.token)
