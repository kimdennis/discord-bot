import discord
from discord.ext import commands

client = commands.Bot(command_prefix='--')

TOKEN = ''  # Get at discordapp.com/developers/applications/me

@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title = "Current Version", description = "The bot is in version 1.0", color=0x00ff00)
    myEmbed.add_field(name = "Version Code", value = "v1.0.0", inline = False)
    myEmbed.add_field(name = "Date Released", value = "July 18th 2020", inline = False)
    myEmbed.set_footer(text= "This is a sample footer") 
    myEmbed.set_author(name = "Dennis")


    await context.message.channel.send(embed=myEmbed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! {round(client.latency * 1000)}ms')

@client.event
async def on_ready():
    
    general_channel = client.get_channel(871918917478658050)
    await general_channel.send('Hello, world!')

@client.event
async def on_disconnect():
    general_channel = client.get_channel(871918917478658050)
    await general_channel.send('Goodbye!')

@client.event
async def on_message(message):

    if message.content == 'what is the version':
        general_channel = client.get_channel(871918917478658050)

        myEmbed = discord.Embed(title = "Current Version", description = "The bot is in version 1.0", color=0x00ff00)
        myEmbed.add_field(name = "Version Code", value = "v1.0.0", inline = False)
        myEmbed.add_field(name = "Date Released", value = "July 18th 2020", inline = False)
        myEmbed.set_footer(text= "This is a sample footer") 
        myEmbed.set_author(name = "Dennis")

        await general_channel.send(embed = myEmbed)\

    await client.process_commands(message)


client.run(TOKEN)
