
from credentials import *


import asyncio
import re
import textwrap

import discord
import twitter



class Bot(discord.Client):
    def __init__(self, **kwargs):
        super().__init__()
        self.api = twitter.Api(**kwargs, sleep_on_rate_limit=True)
    def run(self, email=None, password=None):
        super().run(email, password)

    def retweet(self, msg):
        if msg.channel.id == '293416436620197889' and 'tweet à rt' in msg.content.lower():
            try:
                status = self.api.GetStatus(re.search(r'(?<=/)\d{18}', msg.content).group())
                if not status.retweeted:
                    self.api.PostRetweet(status.id)

                    text = textwrap.indent(textwrap.fill(status.text), '    ')
                    print('  \033[1m@%s\033[0;92m\n%s\033[0m\n' % (status.user.name, text))
            except Exception as e:
                print('\n\033[1;31m%s: %s\033[0m\n' % (type(e).__name__, e))
        elif msg.channel.id == '256392899720249344':
            for link in re.findall(r'https?://\S+', msg.content):
                try:
                    self.api.PostUpdate(link)
                    print('\033[36m%s\033[0m\n' % link)
                except Exception as e:
                    print('\n\033[1;31m%s: %s\033[0m\n' % (type(e).__name__, e))

    async def on_ready(self):
        for channel in self.get_all_channels():
            if channel.id in ('293416436620197889', '256392899720249344'):
                async for msg in self.logs_from(channel, limit=16):
                    self.retweet(msg)
    async def on_message(self, msg):
        self.retweet(msg)

Bot(**twitter_credentials).run(**discord_credentials)
