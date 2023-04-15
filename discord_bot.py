import os
import discord
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()

import requests
import json



intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期

@tree.command(name="create",description="create shishiodoshi")
async def test_command(interaction: discord.Interaction,people: int, chain: str, bet: float, min_token: int):
    embed = discord.Embed(title="game setting", color=0x00ff00)
    embed.add_field(name="number of participantes", value=f"{people}人", inline=False)
    embed.add_field(name="chain", value=chain, inline=False)
    embed.add_field(name="bet increment", value=f"{bet} tokens", inline=False)
    embed.add_field(name="minimum amount of token", value=f"{min_token} tokens", inline=False)

    await interaction.response.send_message(embed=embed)
    print(people, chain, bet, min_token)


    # JSONデータ
    data = {
        "ChainName":"chain",
        "BidIncrement":bet,
        "BidToken":"sso",
        "Playercount":people,
        "StartingCoinAmount":min_token
    }

    # JSONデータを文字列に変換
    json_data = json.dumps(data)

    # POSTリクエストのURL
    url = "http://142.132.149.187:8082/newGame"

    # POSTリクエストを送信
    response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

    # レスポンスを表示
    print(response.text)

    

    url = "https://discord.com/api/webhooks/1096866903730950174/Ali8xmv4UBa95-kmna133OkFdiayHZjKp_2D8rkLSmkm41808tyfzKKUtd5pCnTyRSn7"
    payload = {"username": "Game Starter", "content": "https://shishiodoshi-app-k22f.vercel.app/game/11/"}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
    else:
        print("Error: ", response.status_code)


client.run(os.getenv('TOKEN'))



