import datetime
from discord import client
import discord
import json
from config import TOKEN
from discord.ext import commands

with open('data.json') as json_file:
    data = json.load(json_file)

def embedNextFilm(obj, ctx):

    # Create an embedded message
    embed = discord.Embed(title=(obj['title']))

    embed.set_thumbnail(url=ctx.author.avatar.url)

    # Add the string to the embedded message
    embed.add_field(name="**Date**", value=obj['date'], inline=False)
    embed.add_field(name="**Hour**", value=obj['hour'], inline=False)
    embed.add_field(name="**Added by**", value=obj['addedBy'], inline=False)

    # Set the image URL as the thumbnail
    embed.set_thumbnail(url=obj['image'])

    return embed

async def events(data, ctx):
    embeds = []

    for obj in data:
        # Create an embedded message
        embed = discord.Embed(title=(obj['title']))
        
        channel = ctx.channel  #gets the channel you want to get the list from

        members = channel.members #finds members connected to the channel

        member = next((x for x in members if x.name == obj['addedBy']), None)

        print(members)

        embed.set_thumbnail(url=member.author.avatar.url if member != None else '')

        # Add the string to the embedded message
        embed.add_field(name="**Date**", value=obj['date'], inline=False)
        embed.add_field(name="**Hour**", value=obj['hour'], inline=False)
        embed.add_field(name="**Added by**", value=obj['addedBy'], inline=False)

        # Set the image URL as the thumbnail
        embed.set_image(url=obj['image'])
    
        await ctx.send(embed=embed)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_guild_join(guild):
    channel = guild.text_channels[0]
    await channel.send("Hola soy un bot que puede recordarte eventos. Pídeme lo que quieras!!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command(pass_context=True, name='hello')
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith("!events"):
        await message.channel.send(embed=events(data))

@bot.command(pass_context=True, name='addFilm')
async def _addFilm(ctx, *args):
    film = {
        'title': args[0],
        'date': args[1],
        'hour': args[2],
        'image': args[3],
        'addedBy': ctx.author.name
    }

    data.append(film)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    await ctx.send(args[0] + " added")

@bot.command(pass_context=True, name='nextFilm')
async def _nextFilm(ctx):
    CONST_TIME_NOW = datetime.now()

    with open('data.json', 'r') as file:
        data = json.load(file)

    nextFilm = None 

    for obj in data:

        if(nextFilm == None):
            nextFilm = obj
    
        if(nextFilm['date'] > obj['date'] and obj['date'] >= CONST_TIME_NOW):
            nextFilm = obj
        elif(nextFilm['date'] == obj['date'] and nextFilm['hour'] > obj['hour']):
            nextFilm = obj

    await ctx.send(embed=embedNextFilm(nextFilm, ctx))
    
@bot.command(pass_context=True, name='events')
async def _events(ctx):
    with open('data.json', 'r') as file:
        data = json.load(file)

    await events(data, ctx)
    
bot.run(TOKEN)