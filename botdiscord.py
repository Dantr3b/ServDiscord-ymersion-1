import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'test':
            await message.channel.send('sa marche')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTE1NDc2NzM0NjEyMTA2MDQwMw.G5X95G.Hj89qS7tdiRWfxytvlLVZWFV-Vn20TDNeWaYUc')