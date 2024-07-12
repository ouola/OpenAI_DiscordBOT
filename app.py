from app import app
from flask import Flask, request, abort


import discord
from discord.ext import commands , tasks 


#======python的函數庫==========
import tempfile, os
import datetime
import openai
import time
import traceback
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Disocrd Bot Key
Discord_token = os.getenv('DISCORD_TOKEN')
# OPENAI API Key初始化設定
openai.api_key = os.getenv('OPENAI_API_KEY')

def GPT_response(text):
    # 接收回應
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=text, temperature=0.5, max_tokens=500)
    print(response)
    # 重組回應
    answer = response['choices'][0]['text'].replace('。','')
    return answer






intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents = intents)


@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")





@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to avoid infinite loops
    if message.author == bot.user:
        return
    try:

        if message.content:
            GPT_answer = GPT_response(message.content)

            await ctx.send(GPT_answer)
    except:
        print(traceback.format_exc())
        await ctx.send('你所使用的OPENAI API key額度可能已經超過，請於後台Log內確認錯誤訊息')



@bot.command()
async def h(ctx):
    await ctx.send("Hi")


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run(Discord_token)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    discordAIchatbot.run(host='0.0.0.0', port=port)
