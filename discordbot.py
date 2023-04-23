import discord
import typing
import functools

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Client is ready")
    channel = client.get_channel("")
    await channel.send("server started")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        url = message.attachments[0].url
    except IndexError:
        print("No attachments")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            name = message.content.split("**")[1]
            await run_blocking(functionToStore, storage, url, name)

def functionToStore(storage,url, name):
    #TBD
    pass

async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    func = functools.partial(blocking_func, *args, **kwargs) 
    return await client.loop.run_in_executor(None, func)