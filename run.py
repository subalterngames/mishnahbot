import re
import os
from pathlib import Path
from mishnabot.bot import Bot

"""
Run the bot.

Usage:

```
python3 run.py
```
"""


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    secrets = Path(dir_path).joinpath("bot_secrets.txt").read_text()
    # Get the bot token.
    token = re.search(r"token=(.*)", secrets).group(1)
    # Get the Discord channel.
    mishnah_channel = re.search(r"mishnah_channel=(.*)", secrets).group(1)
    try:
        mussar_channel = re.search(r"mussar_channel=(.*)", secrets).group(1)
        mussar_start = re.search(r"mussar_start=(.*)", secrets).group(1)
    except Exception as e:
        mussar_channel = 0
        mussar_start = ""
    bot = Bot(mishnah_channel=int(mishnah_channel), mussar_channel=int(mussar_channel), mussar_start=mussar_start)
    bot.run(token)
