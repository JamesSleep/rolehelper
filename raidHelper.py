import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("bot online")


@client.event
async def on_message(message):
    content = message.content
    guild = message.guild
    if content.startswith("!roles"):
        print(message.guild.roles)
    if content.startswith("!역할"):
        commander = "군단장\n\n\n🐮발탄하드\n\n💋비아노말\n\n💄비아하드\n\n🎪쿠크세이튼\n\n♟아브렐슈드 노말\n\n🎲아브렐슈드 하드\n\n\n\n"
        challenge = "기타\n\n\n⚔도전레이드\n\n🏹도전어비스\n\n👶응애도와줘(뉴비도움줄때)"
        embed = discord.Embed(
            title="", description=commander+challenge, color=0x00aaaa)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("🐮")
        await msg.add_reaction("💋")
        await msg.add_reaction("💄")
        await msg.add_reaction("🎪")
        await msg.add_reaction("♟")
        await msg.add_reaction("🎲")
        await msg.add_reaction("⚔")
        await msg.add_reaction("🏹")
        await msg.add_reaction("👶")


@client.event
async def on_raw_reaction_add(payload):
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)
    roles = guild.roles
    role_name = ""
    role_id = 0
    if payload.member.bot == 1:
        return None
    if str(payload.emoji.name) == "🐮":
        role_name = "발탄하드"
    if str(payload.emoji.name) == "💋":
        role_name = "비아노말"
    if str(payload.emoji.name) == "💄":
        role_name = "비아하드"
    if str(payload.emoji.name) == "🎪":
        role_name = "쿠크세이튼"
    if str(payload.emoji.name) == "♟":
        role_name = "아브렐슈드 노말"
    if str(payload.emoji.name) == "🎲":
        role_name = "아브렐슈드 하드"
    if str(payload.emoji.name) == "⚔":
        role_name = "도전레이드"
    if str(payload.emoji.name) == "🏹":
        role_name = "도전어비스"
    if str(payload.emoji.name) == "👶":
        role_name = "응애도와줘"
    if role_name == "":
        return None
    for i in range(len(roles)):
        if (roles[i].name == role_name):
            role_id = roles[i].id
            return await payload.member.add_roles(client.get_guild(guild_id).get_role(role_id), reason="역할부여")


@client.event
async def on_raw_reaction_remove(payload):
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)
    user = guild.get_member(payload.user_id)
    roles = guild.roles
    role_name = ""
    role_id = 0
    if str(payload.emoji.name) == "🐮":
        role_name = "발탄하드"
    if str(payload.emoji.name) == "💋":
        role_name = "비아노말"
    if str(payload.emoji.name) == "💄":
        role_name = "비아하드"
    if str(payload.emoji.name) == "🎪":
        role_name = "쿠크세이튼"
    if str(payload.emoji.name) == "♟":
        role_name = "아브렐슈드 노말"
    if str(payload.emoji.name) == "🎲":
        role_name = "아브렐슈드 하드"
    if str(payload.emoji.name) == "⚔":
        role_name = "도전레이드"
    if str(payload.emoji.name) == "🏹":
        role_name = "도전어비스"
    if str(payload.emoji.name) == "👶":
        role_name = "응애도와줘"
    if role_name == "":
        return None
    for i in range(len(roles)):
        if (roles[i].name == role_name):
            role_id = roles[i].id
            return await user.remove_roles(client.get_guild(guild_id).get_role(role_id), reason="역할제거")

client.run('')
