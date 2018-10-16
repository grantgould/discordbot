import os
import discord
import asyncio

print("Discord Version: {} ".format(discord.__version__))

class App(discord.Client):
    async def on_ready(self):
        print("Logged in as {} with ID {}".format(self.user.name, self.user.id))

    async def on_message(self, message):
        print("{}: {}: {}: {}".format(message.channel, message.author, message.author.name, message.content ))
        if message.author == self.user:
            return 

        elif message.content.startswith('!meme'):
            await channel.send(file=discord.File('meme.jpg'))

        elif message.content.startswith('!alert'):
            await message.channel.send('ALERT')
        
        elif message.content.startswith('!sleepy'):
            await message.channel.send('Is sleepy...')

        elif message.content.startswith('!logout'):
            await self.close()

# Client Token
token = os.environ['token']

# Asign Lowercase App Name
app = App()

# Run App with Token
app.run(token)