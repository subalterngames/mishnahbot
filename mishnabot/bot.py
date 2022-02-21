from time import sleep
from pathlib import Path
from pkg_resources import resource_filename
from json import loads
from random import Random
import discord


class Bot(discord.Client):
    """
    Post a random mishnah sugye every day.
    """

    def __init__(self, channel: int, seed: int = None):
        """
        :param channel: The ID of the channel.
        :param seed: The seed. If None, the seed is random.
        """

        self.channel: int = channel
        self.mishnah = loads(Path(resource_filename(__name__, "data/mishnah.json")).read_text())
        if seed is None:
            self.rng = Random()
        else:
            self.rng = Random(seed)
        super().__init__()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # Connect to the Discord channel.
        channel = self.get_channel(self.channel)
        while True:
            # Get a random sugye.
            sugye = self.mishnah[self.rng.randint(0, len(self.mishnah) + 1)]
            url = f"https://www.sefaria.org/Mishnah_{sugye['Order'].replace(' ', '_')}.{sugye['Chapter']}.{sugye['Verse']}?lang=bi"
            # Get the English text. Convert HTML tags to markdown tags.
            en = sugye['en'][:]
            en = en.replace("<b>", "**").replace("</b>", "**").replace("<i>", "_").replace("</i>", "_")
            # Create a citation.
            citation = f"{sugye['Order']} {sugye['Chapter']}.{sugye['Verse']}"
            # Get the text.
            he = sugye["he"]
            text = f"**{citation}**\n{he}\n{en}\n{url}"
            # Split the text into posts of <= 2000 characters.
            posts = [text[index: index + 2000] for index in range(0, len(text), 2000)]
            # Post.
            for post in posts:
                await channel.send(post)
            # Wait a day.
            sleep(86400)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
