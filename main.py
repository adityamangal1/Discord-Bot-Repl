from keep_alive import keep_alive

import discord
from discord.ext import commands
import requests
import random
import os


client = discord.Client()


@client.event
async def on_connect():
    print("Yes, I am connected")


@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::-1])


@client.event
async def on_message(message):
    jokes_list = ['I invented a new word! Plagiarism! 😛', 'Why did the chicken go to the séance? To get to the other side 😛.',
                  'Where are average things manufactured? The satisfactory. 😛', 'What sits at the bottom of the sea and twitches? A nervous wreck. 😛', 'Why do we tell actors to “break a leg?” Because every play has a cast. 😉']
    meme_list = ['https://static.mommypoppins.com/styles/image620x420/s3/school_meme_3_1.jpg?itok=zJWEcZFx',
                 'https://www.dailymoss.com/wp-content/uploads/2018/05/IMG-2067.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ16EULL7pZIkji05u0_FWzCLZZHj538fJ781UjG-ZHhCSQ5uQ7e9WdJpcpf6R28PGNuN0&usqp=CAU', 'https://i.redd.it/lmc0p77kifl61.jpg', 'https://i.redd.it/o5693es1gtz31.jpg', 'http://www.ulikes.in/web-app/users_data/2810/exams_data/images/KHIDKI1618133491k2810y1054.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4iFkyyQ9WmOikRXIGHTMlnZYx3T-0tTj2PA&usqp=CAU']
    gif_list = ['https://i.pinimg.com/originals/5d/0f/01/5d0f017723d610ab01c01c1d6ea87f9f.gif',
                'https://media3.giphy.com/media/SggILpMXO7Xt6/giphy.gif', 'https://i.pinimg.com/originals/ae/c0/44/aec0445c6b1673136db065b176d1e888.gif', 'https://i.pinimg.com/originals/c5/c2/f7/c5c2f72d38488ea6ef140b13a70906ad.gif']
    if message.content.startswith('-hello') or message.content.startswith('-hi'):
        await message.add_reaction("❤️")
        await message.channel.send("kem cho mota bhai? 😆")
    elif message.content.startswith('-how are you'):
        await message.add_reaction("❤️")
        await message.channel.send("Fine! How about you Sir? 😀")
    elif message.content == '-private':
        await message.add_reaction("😀")
        await message.channel.send("Check Dm sir 😉")
        await message.author.send("We are in private space now!Yes Sir?")
    elif message.content.startswith('-joke'):
        await message.add_reaction("😀")
        rand_jokes = random.choice(jokes_list)
        await message.channel.send(rand_jokes)
    elif message.content.startswith('-meme'):
        await message.add_reaction("🤪")
        rand_meme = random.choice(meme_list)
        await message.channel.send(rand_meme)
    elif message.content.startswith('-gif'):
        await message.add_reaction("🤪")
        gif = random.choice(gif_list)
        await message.channel.send(gif)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
