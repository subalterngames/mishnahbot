import re
from pathlib import Path
from mishnabot.bot import Bot

if __name__ == "__main__":
    q = Path("secrets.txt").read_text()
    token = re.search(r"token=(.*)", q).group(1)
    channel = int(re.search(r"channel=(.*)", q).group(1))
    bot = Bot(channel=channel)
    bot.run(token)
