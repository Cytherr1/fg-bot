import discord
import responses
import openai
from discord import Embed, Colour


async def send_message(message, user_message, channel, is_private):
    try:
        response = responses.handle_response(user_message, channel)
        if user_message.startswith('f!stats'):
            await message.author.send(response) if is_private else await message.channel.send(response, embed=Embed(
                colour=Colour.blue(),
                description="test",
            ))
        elif user_message.startswith('f!play'):
            await message.author.send(response) if is_private else await message.channel.send(response, embed=Embed(
                title="Now playing:",
                colour=Colour.blue(),
                description="test",
            ))
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = DISCORD_TOKEN
    openai.api_key = OPENAI_API_KEY
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} in {channel}')

        if user_message[0] == '?':
            await send_message(message, user_message, channel=channel, is_private=True)
        else:
            await send_message(message, user_message, channel=channel, is_private=False)

    client.run(TOKEN)
