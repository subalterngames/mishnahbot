from pathlib import Path
from os import getcwd
from pkg_resources import resource_filename
from json import loads
import random
from datetime import datetime
import discord


class Bot(discord.Client):
    """
    Post a random mishnah sugye every day.
    """

    def __init__(self, mishnah_channel: int, mussar_channel: int, mussar_start: str, logging: bool = True):
        """
        :param mishnah_channel: The ID of the channel for posting Mishnah.
        :param mussar_channel: The ID of the channel for posting Mussar
        :param mussar_date: The start date in ISO format for the daily mussar practice
        :param logging: If True, log messages.
        """

        self.mishnah_channel: int = int(mishnah_channel)
        self.mishnah = loads(Path(resource_filename(__name__, "data/mishnah.json")).read_text())
        self.mussar_channel: int = int(mussar_channel)
        self.mussar_start: str = mussar_start
        self.mussar_text = loads(Path(resource_filename(__name__, "data/every-day-holy-day.json")).read_text())
        self.logging: bool = logging
        super().__init__()


    async def post_mishnah(self):
        # Connect to the Discord channel.
        channel = self.get_channel(self.mishnah_channel)
        today = datetime.today()
        # Get a random sugye.
        sugye = self.mishnah[random.randint(0, len(self.mishnah) + 1)]
        url = f"https://www.sefaria.org/Mishnah_{sugye['Order'].replace(' ', '_')}.{sugye['Chapter']}.{sugye['Verse']}?lang=bi"
        # Get the English text. Convert HTML tags to markdown tags.
        en = sugye['en'].replace("<b>", "**").replace("</b>", "**").replace("<i>", "_").replace("</i>", "_")
        # Create a citation.
        citation = f"{sugye['Order']} {sugye['Chapter']}.{sugye['Verse']}"
        self.log(f"{today}: {citation}")
        # Get the text.
        he = sugye["he"]
        text = f"**{citation}**\n{he}\n{en}\n{url}"
        # Split the text into posts of <= 2000 characters.
        posts = [text[index: index + 2000] for index in range(0, len(text), 2000)]
        try:
            # Post.
            for post in posts:
                await channel.send(post)
        except Exception as e:
            self.log(str(e))


    async def post_mussar(self):
        # Connect to the Discord channel.
        channel = self.get_channel(self.mussar_channel)

        # Calculate the week & day of the practice
        today = datetime.today()
        start_date = datetime.fromisoformat(self.mussar_start)
        delta = today - start_date
        if delta.days < 0: return  # We haven't started yet
        week = str(((delta.days // 7) % 52) + 1)  # Indexed from 1
        day = str((delta.days % 7) + 1)

        # Construct the text
        post = [f"Daily mussar for {today.strftime('%a %b %d, %Y')}"]
        post.append(f">>> **Week {week}: {self.mussar_text[week]['title'].title()}**")
        post.append(f"Day {day}")
        post.append("\n".join(self.mussar_text[week]['day_texts'][day]))
        post.append(f"Focus Phrase: {self.mussar_text[week]['phrase']}")
        post.append(f"Practice: {self.mussar_text[week]['practice']}")
        post_str = "\n\n".join(post)

        # Post
        try:
            await channel.send(post_str)
        except Exception as e:
            self.log(str(e))


    async def on_ready(self):
        await self.post_mishnah()
        if self.mussar_channel and self.mussar_start:
            await self.post_mussar()
        await self.close()


    def log(self, message: str) -> None:
        """
        Log a message.

        :param message: The message.
        """

        if self.logging:
            with Path(getcwd()).joinpath("log.txt").open("at") as f:
                f.write(message + "\n")
