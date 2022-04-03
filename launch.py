import re
from pathlib import Path
from mishnabot.ssh import ssh


"""
Run mishnabot on a remote server. This assumes that you've already uploaded it (see `ftp.py`).

This reads from a file called secrets.txt located in the same directory as this file. The secrets.txt file must contain this information:

```
token=TOKEN
channel=CHANNEL
ssh_username=USERNAME
ssh_password=PASSWORD
```

`TOKEN` is the bot token. `CHANNEL` is the Discord channel ID.
"""

if __name__ == "__main__":
    secrets = Path("secrets.txt").read_text()
    # Get the bot token.
    token = re.search(r"token=(.*)", secrets).group(1)
    # Get the Discord channel.
    channel = re.search(r"channel=(.*)", secrets).group(1)
    # Spawn a daemon process and run the bot.
    ssh(command=["python3", "run.py",
                 "--token", token,
                 "--channel", channel,
                 "--shomer",
                 "--shabbos", str(6),
                 "--logging"],
        cwd=re.search(r"ssh_cwd=(.*)", secrets).group(1),
        daemon=True)
