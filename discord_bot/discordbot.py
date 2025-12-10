import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import datetime
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VOICE_CHANNEL_ID_Lounge = int(os.getenv("VOICE_CHANNEL_ID_Lounge"))
TEXT_CHANNEL_ID_Genral = int(os.getenv("TEXT_CHANNEL_ID_Genral"))
VOICE_CHANNEL_ID_Study1 = int(os.getenv("VOICE_CHANNEL_ID_Study1"))

import config

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',
                   intents = intents)

greeted_users = {}

omikuji = ["大吉", "小吉", "マジ吉", "凶", "大凶", "吉", "中吉", "ま...まあ（笑）",
           "ま！！？", "lucky!!", "12位", "最下位", "C賞", "D賞", "おみくじ信じてるのマ！？"
           ,"参加賞", "大凶", "爆死", "天井","すりぬけ", "今日は単発でフェス限あたるよ！"
           ,"ゴミ席", "今日は家にいよっか、、、", "最低保証", "はずれ"]

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    print('bot is ready to receive commands.')
    for channel in bot.get_all_channels():
        print(channel.name + "," + str(channel.id))

now = datetime.datetime.now()
print(now.hour)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    today = datetime.date.today()
    user_id = message.author.id
    
    if greeted_users.get(user_id) == today:
        # if message.content == "おみくじ":
        #     content = random.choice(omikuji)
        #     await message.channel.send(content)
        # elif message.content == "おはよう":
        #     await message.channel.send("おはよう！！")
        await Omikuji(message)
        return
    
    greeted_users[user_id] = today

    print(f"{message.author}よりメッセージを受信しました:{message.content}")
    if 4 <= now.hour and now.hour <=10:
        await message.channel.send("おはよう！")
    else:
        await message.channel.send("こんばんわ！")
    
    await Omikuji(message)

    # if message.content == "おみくじ":
    #    content = random.choice(omikuji)
    #    await message.channel.send(content)
    # elif message.content == "おはよう":
    #     await message.channel.send("おはよう！！")

async def Omikuji(message):
    if message.content == "おみくじ":
       content = random.choice(omikuji)
       await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")


#ボイスチャットに入ったとき通知してくれるコード　is not None 変数がNoneかNoneじゃないか判定するためにつかう
@bot.event
async def on_voice_state_update(user, before, after):
    if before.channel !=after.channel:#ユーザーがボイスチャンネルを移動したか判別
        botRoom = bot.get_channel(TEXT_CHANNEL_ID_Genral)
        if after.channel is not None and after.channel.id == VOICE_CHANNEL_ID_Lounge:
            await botRoom.send("**" + after.channel.name +"** で！__" + user.display_name+  "__がプログラミング学習を始めました！！")

@bot.event
async def on_voice_state_update(user, before, after):
    if before.channel !=after.channel:#ユーザーがボイスチャンネルを移動したか判別
        botRoom = bot.get_channel(TEXT_CHANNEL_ID_Genral)
        if after.channel is not None and after.channel.id == VOICE_CHANNEL_ID_Study1:
            await botRoom.send("**" + after.channel.name +"** で現在__" + user.display_name+  "__現実逃避で！スタレはじめちゃいました！！")


@bot.command()
async def hello(ctx):
    await ctx.send(f"こんにちわ、{ctx.author.display_name}さん！")

@bot.event
async def ping(ctx):
    await ctx.send(f"Pong!{round(bot.latency * 1000)}ms")


bot.run(config.DISCORD_TOKEN)