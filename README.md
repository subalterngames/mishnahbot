# Mishnabot

Discord bot that posts a random mishnah sugye once a day.

![](logo.png)

# Requirements

- A remote server
- On your computer, git and Python 3.6 or newer
- On the server, Python 3.6 or newer

# Setup

## 1. Discord

1. [Create a Discord bot.](https://gizmodo.com/how-to-make-a-discord-bot-1847378375)
2. [Get the ID of the channel you want the bot to post to.](https://docs.statbot.net/docs/faq/general/how-find-id/)
3. Get the OAuth2 client ID of the bot (you'll need this in order to add it to the channel).
3. Add the bot to the channel.

## 2. Your remote server

1. Get Python running on your server. How to do this will vary depending on the webhost.
2. Make sure you can ftp and ssh into the server.

## 3. Your local computer

1. Clone this repo. The rest of this documentation assumes that you've cloned the repo to `~/mishnabot` where `~` is your home directory.
2. Create a file named `secrets.txt` in the same directory as this file, formatted like this:

```
token=BOT_TOKEN
channel=CHANNEL_ID
ssh_username=USERNAME
ssh_password=PASSWORD
ftp_username=USERNAME
ftp_password=PASSWORD
ftp=ftp.subalterngames.com
hostname=talmud.subalterngames.com
ssh_cwd=talmud.subalterngames.com/public
```

In a terminal:

1. `cd ~/mishnabot`
2. `python3 ftp.py` This will upload mishnabot to your server. On Windows, run `py -3 ftp.py` instead.
3. `ssh USERNAME@SERVER` 
4. `cd path/to/mishnabot`
5. `python3 -m pip install -e .`
6. `exit`
7. `python3 ssh.py` This will start running the bot. On Windows, run `py -3 ssh.py` instead.