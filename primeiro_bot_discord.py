import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(
    'MTA3MzMwNjMzNTE4NzMyMTA1Mw.G5Icqv.ngms7VZdNPZJGEVWsoomhkNahtPMPR2mYwFYcQ')
