import discord
import weather

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(";오늘날씨"):
        msg1=await message.channel.send("날씨를 불러오고 있습니다.")
        embed = discord.Embed(
            title="오늘의 날씨",
            color=0xd0eFF0,
        )
        data=weather.getWeatherToday()
        for i in data:
            if data[i]==None:
                continue
            embed.add_field(name=f'{i}시', value="", inline=False)
            embed.add_field(name="",value="습도 : "+data[i]['REH'], inline=True)
            embed.add_field(name="",value="기온 : "+data[i]['T1H'], inline=True)
            embed.add_field(name="",value="강수 : "+data[i]['RN1'], inline=True)

        await msg1.delete()
        await message.channel.send(embed=embed)
    if message.content.startswith(";그때날씨"):
        arg=message.content[6:]
        if arg=="":
            await message.channel.send("인자 형태 : YYYYMMDD")
            return
        msg1=await message.channel.send("날씨를 불러오고 있습니다.")
        embed = discord.Embed(
            title="그때의 날씨",
            color=0xd0eFF0,
        )
        data=weather.getWeatherThen(arg)
        for i in data:
            if data[i]==None:
                continue
            embed.add_field(name=f'{i}시', value="", inline=False)
            embed.add_field(name="",value=f"습도 : {data[i]['REH']}%", inline=True)
            embed.add_field(name="",value=f"기온 : {data[i]['T1H']}℃", inline=True)
            embed.add_field(name="",value=f"강수 : {data[i]['RN1']}㎜", inline=True)

        await msg1.delete()
        await message.channel.send(embed=embed)

client.run("token")
