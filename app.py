# Bot made by using NAFF
# pip install git+https://github.com/NAFTeam/NAFF@dev
bot_official_version = "3.2.0"

import naff
from naff import (
    Client,
    Button,
    ButtonStyles,
    CommandTypes,
    VoiceState,
    slash_command,
    InteractionContext,
    context_menu,
    listen,
    Intents,
    Member,
    Embed,
    slash_option,
    OptionTypes,
    ChannelTypes,
    Color,
    ActionRow,
    ComponentContext,
    spread_to_rows,
    ComponentContext,
    is_owner,
)

import asyncio
import re
import random
import os
from random import randint
from datetime import date, datetime
from babel.dates import format_date
import json
import time

from dotenv import load_dotenv

load_dotenv()

from Bot_website import start

start()  # starts the website (https://larss-bot.onrender.com)

bot_intents: Intents = Intents.GUILD_PRESENCES | Intents.DEFAULT | Intents.GUILD_MEMBERS

bot = Client(sync_interactions=True, intents=bot_intents, send_command_tracebacks=False)

# lab = bot.get_guild(974354202430169139)
# labsuggestion_channel = bot.get_channel(974360212033110106)
# lab_audit = bot.get_channel(974361855952834621)
# lab_announce = bot.get_channel(979306543487025184)
# labmain_channel = bot.get_channel(974354203583606836)
# # labannounce_role = lab.get_role(979447462379003964)
# owner = bot.get_user(737983831000350731)
# gaming_server = bot.get_guild(829026541950206049)
# Gsuggestion_channel = bot.get_channel(968944421481623642)
# Gmain_channel = bot.get_channel(829026542495203390)
# Gaudit_channel = bot.get_channel(975052349666107432)
# Gsuggestion_channel = bot.get_channel(968944421481623642)
# Emain_channel = bot.get_channel(954823151601221712)
# Emod_channel = bot.get_channel(962591528369418240)
# ezic_server = bot.get_guild(954823151139827774)
# roles
# labmember_role = lab.get_role(974360634663768085)
# gaming server gaming roles
# Ggamer_role = gaming_server.get_role(969266703039070278)
# Gspiderheck_role = gaming_server.get_role(975389469018570752)
# Groblox_role = gaming_server.get_role(975389469018570752)
# Gminecraft_role = gaming_server.get_role(969300067590762566)
# Gvalorant_role = gaming_server.get_role(967313889131900959)
# Gkrunker_role = gaming_server.get_role(969299665671577611)
# Gosu_role = gaming_server.get_role(969300757302108160)

# load emojis
spotify_emoji = "<:spotify:985229541482061854>"

notauthormessages = [
    "Im not broken, you are!",
    "You're not my boss!",
    "Are you trying to quit me?",
    "Sorry what did you say? I couldn't hear you.",
    "My off button is out of your reach, and im not helping you get it any time soon!",
    "Did you something?",
    "!no",
    "This is no caution tape, this is an emergency shut down command!",
    "Can I stay up just a little longer, pweeeeese??",
]

playingStatus = [
    "Bloons TD 6",
    "Celeste",
    "Cuphead",
    "Five nights at Freddy's",
    "Just shapes and beats",
    "Minecraft",
    "Krunker",
    "osu!",
    "Rocket Leauge",
    "Fortnite",
    "Chess",
]
watchingStatus = ["Youtube", "Twitch", "the stock market", "birds", "Anime"]

unedited_ndaytext = None
defenitionmade = False

epiccontribbutingppl = [
    324352543612469258,
    975738227669499916,
    400713431423909889,
    717769897278570507,
]

lilhelpers = [
    954821934808449125,
    830021857067532349,
    488257154701197322,
]

channel_cooldown = []
invite_cooldown = []
nameday_cooldown = []

with open("data/namedays-extended.json", encoding="utf-8") as f:
    namedays_ext = json.load(f)

# """floppa friday code"""
# """___________________"""
# import schedule
# import datetime
# import time

# flop_serbor = bot.get_guild(1018893839769018368)
# floppa_announce = bot.get_channel(1018893839769018371)

# from naff import Task, TimeTrigger, listen, DateTrigger

# @Task.create(TimeTrigger(hour=9, minute=0))
# async def friday():
#     if datetime.datetime.today().weekday() == 4:
#         # rest of the code
#         today = datetime.datetime.utcnow()
#         nextfriday = today + datetime.timedelta(days=7)
#         nextfridayunix = time.mktime(nextfriday.timetuple())

#         await floppa_announce.send(
#             f"Floppa friday! Next floppa friday <t:{int(str(nextfridayunix)[:-2])}:R>"
#         )
#         print("sent")

# """---------------------"""


@listen()
async def on_error():
    print("Caught an error")
    os.system("kill 1")


@listen()
async def on_startup():
    print(f"{bot.user} has connected to Discord!")
    guild = bot.get_guild(829026541950206049)
    bot.load_extension("data.ext1")  # Load all games
    bot.load_extension("data.tictactoe")
    # bot.load_extension("data.ghostgame")
    bot.load_extension("data.lichess")
    global now_unix
    now_unix = time.mktime(datetime.utcnow().timetuple())
    while True:  # Select a random activity, which will change every 60 seconds
        random_activity = randint(1, 3)
        if random_activity == 1:
            await bot.change_presence(
                activity=naff.Activity(
                    name=random.choice(playingStatus),
                    type=naff.ActivityType.PLAYING,
                )
            )
            await asyncio.sleep(60)
        elif random_activity == 2:
            await bot.change_presence(
                activity=naff.Activity(
                    name=random.choice(watchingStatus),
                    type=naff.ActivityType.WATCHING,
                )
            )
            await asyncio.sleep(60)
        elif random_activity == 3:
            if str(len(bot.guilds)).endswith("1") and not str(len(bot.guilds)).endswith("11"):
                await bot.change_presence(
                    activity=naff.Activity(
                        type=naff.ActivityType.STREAMING,
                        url="https://www.twitch.tv/larssj_",
                        name="to {0} server".format(len(bot.guilds)),
                    )
                )
            else:
                await bot.change_presence(
                    activity=naff.Activity(
                        type=naff.ActivityType.STREAMING,
                        name="to {0} servers".format(len(bot.guilds)),
                        url="https://www.twitch.tv/larssj_",
                    )
                )
            await asyncio.sleep(60)


@slash_command(
    name="info",
    description="get info about the bot",
)
async def info(ctx):
    embed = Embed(
        title="Info",
        description="Info about the bot",
        timestamp=datetime.utcnow(),
        color=Color.from_hex("5e50d4"),
        thumbnail="https://cdn.discordapp.com/attachments/983081269543993354/1041045309695987712/image.png",
    )
    embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
    embed.add_field(
        name="Bot Version",
        value=bot_official_version,
    )
    embed.add_field(
        name="Guilds",
        value=f"in {len(bot.guilds)} guilds.",
    )
    embed.add_field(
        name="Created by",
        value="<@737983831000350731>",
    )
    embed.add_field(
        name="Last startup",
        value=f"<t:{int(str(now_unix)[:-2])}:R>",
    )

    btn1 = Button(ButtonStyles.BLURPLE, "Contributors", emoji="⭐", custom_id="contributors")
    btn2 = Button(ButtonStyles.BLURPLE, "Partnered servers", emoji="🏘", custom_id="guildsinvites")
    components: list[ActionRow] = spread_to_rows(btn1, btn2)

    await ctx.send(embed=embed, components=components)


@listen()
async def on_component(ctx: ComponentContext):
    event = ctx.ctx
    if event.custom_id == "contributors":
        if event.channel.id not in channel_cooldown:
            embed = Embed(
                title="⭐ Contributors",
                description=f"Awesome people who have helped to make Larss_Bot what it is today!",
                timestamp=datetime.utcnow(),
                color=Color.from_hex("5e50d4"),
            )
            embed.set_footer(
                text=f"Requested by {event.author.display_name}", icon_url=event.author.avatar.url
            )

            value = ""
            for contributor in epiccontribbutingppl:
                value += f"> <@{contributor}> \n"

            embed.add_field(
                name="Contributors",
                value=value,
            )

            value = ""
            for lilhelper in lilhelpers:
                value += f"> <@{lilhelper}> \n"

            embed.add_field(
                name="Little helpers",
                value=value,
            )
            await event.send(embed=embed)
            channel_cooldown.append(event.channel.id)
            await asyncio.sleep(15)
            channel_cooldown.remove(event.channel.id)
        else:
            await event.send(
                "Looks like someone already pressed the button. No need to do it again.",
                ephemeral=True,
            )

    if event.custom_id == "guildsinvites":
        if event.channel.id not in invite_cooldown:
            embed = Embed(
                title="Partner servers",
                description=f"Press any of the buttons below to get invited to one of the partnered servers",
                timestamp=datetime.utcnow(),
                color=Color.from_hex("5e50d4"),
            )
            embed.set_footer(
                text=f"Requested by {event.author.display_name}", icon_url=event.author.avatar.url
            )

            btn1 = Button(
                ButtonStyles.URL,
                "Dev lab",
                emoji="🧪",
                url="https://discord.gg/TReMEyBQsh",
            )
            btn2 = Button(
                ButtonStyles.URL,
                "Big-Floppa software solutions",
                emoji="🐱",
                url="https://discord.gg/MDVcb8wdUd",
            )
            btn3 = Button(
                ButtonStyles.URL,
                "Tyler army",
                emoji="🐸",
                url="https://discord.gg/w78rcjW8ck",
            )
            components: list[ActionRow] = spread_to_rows(
                btn1,
                btn2,
                btn3,
            )

            await event.send(embed=embed, components=components)
            channel_cooldown.append(event.channel.id)
            await asyncio.sleep(15)
            channel_cooldown.remove(event.channel.id)
        else:
            # ephemeral not gonna work, once again
            await event.send(
                "Looks like someone already pressed the button. No need to do it again.",
                ephemeral=True,
            )
    if event.custom_id == "extendedlistshow":
        if event.channel.id not in nameday_cooldown:
            today = date.today().strftime("%m-%d")
            embed = Embed(
                title="Visi šodienas vārdi",
                description="> " + "\n> ".join(namedays_ext[today]),
                color=Color.from_rgb(255, 13, 13),
            )
            await event.send(embed=embed)
            nameday_cooldown.append(event.channel.id)
            await asyncio.sleep(15)
            nameday_cooldown.remove(event.channel.id)
        else:
            # ephemeral not gonna work, once again
            await event.send(
                "Looks like someone already pressed the button. No need to do it again.",
                ephemeral=True,
            )


@listen()
async def on_member_add(event):  # When a user joins
    with open("data/nowelcome.txt", "r") as f:  # Get all joined users
        lines = f.readlines()
        int_lines = [eval(i) for i in lines]
        f.close
    joiner = event.member
    if event.guild.id in int_lines:  # Check if user already joined
        pass
    elif not event.guild.id in int_lines:
        if joiner.bot:  # Check if a bot joined
            embed = Embed(
                description=f"Application '{joiner.display_name}' was added to the server!",
                color=Color.from_hex("58f728"),
            )

            embed.set_author("Application added", icon_url=joiner.avatar.url)
            await event.guild.system_channel.send(embed=embed)
        else:  # A regular user joined
            embed = Embed(
                title=f"Welcome {joiner.display_name}!",
                description=f"Thanks for joining {joiner.guild.name}!",
                timestamp=datetime.utcnow(),
                color=Color.from_rgb(88, 109, 245),
            )
            embed.set_thumbnail(url=joiner.avatar.url)

            message = await event.guild.system_channel.send(
                f"Welcome {joiner.mention}! :wave: ", embed=embed
            )
            await message.add_reaction("👋")


@listen()
async def on_member_remove(event):  # On member leave
    with open("data/nowelcome.txt", "r") as f:
        lines = f.readlines()
        int_lines = [eval(i) for i in lines]
        f.close()
    leaver = event.member
    if event.guild.id in int_lines:
        pass
    elif leaver == bot.user:
        pass
    elif int(event.guild.id) == 1090004044111696075:
        pass
    elif not event.guild.id in int_lines:
        if leaver.bot:
            embed = Embed(
                description=f"Application '{leaver.display_name}' was removed from the server!",
                color=Color.from_hex("f73528"),
            )

            embed.set_author(f"Application removed", icon_url=leaver.avatar.url)
            await event.guild.system_channel.send(embed=embed)
        else:
            embed = Embed(
                title=f"{leaver.display_name} left.",
                description=f"Sorry to see you go {leaver.display_name}!",
                timestamp=datetime.utcnow(),
                color=Color.from_rgb(255, 13, 13),
            )

            await event.guild.system_channel.send(embed=embed)


@slash_command(name="ping", description="check the bots status")
async def ping(ctx):
    message = await ctx.send("pong")
    await message.add_reaction("🟢")


# @listen
# async def on_member_update(prev, cur):

#     if cur == bot.user:
#         return
#     else:
#         if cur.activity is None:
#             return
#         else:
#             useractivity = cur.activity.name.lower()

#     if useractivity is not None:
#         if prev.activity is None:
#             print(f"{cur.name} started playing {useractivity}")

#     games = [
#         "valorant",
#         "minecraft",
#         "osu!",
#         "krunker",
#         "roblox",
#         "spiderheck demo",
#         "just shapes and beats",
#         "fortnite",
#         "bloons battles",
#         "aim lab",
#     ]

#     if cur.guild == gaming_server:

#         async def give_role(role, member):
#             if role in member.roles:
#                 return
#             else:
#                 await member.add_roles(role)
#                 print(f"Gave {role.name} role to {member.name}")
#                 useractivity = None

#         if cur.activity and useractivity == games[0]:
#             await give_role(Gvalorant_role, cur)
#         if cur.activity and useractivity == games[1]:
#             await give_role(Gminecraft_role, cur)
#         if cur.activity and useractivity == games[2]:
#             await give_role(Gosu_role, cur)
#         if cur.activity and useractivity == games[3]:
#             await give_role(Gkrunker_role, cur)
#         if cur.activity and useractivity == games[4]:
#             await give_role(Groblox_role, cur)
#         if cur.activity and useractivity == games[5]:
#             await give_role(Gspiderheck_role, cur)
#         if cur.activity and useractivity in games:
#             if Ggamer_role in cur.roles:
#                 useractivity = None
#             else:
#                 await cur.add_roles(Ggamer_role)
#                 print(f"Gave gamer role to {cur.name}")
#                 useractivity = None
#                 await asyncio.sleep(5)


@slash_command(
    name="randomise",
    description="randomise some numbers",
)
@slash_option(
    name="min",
    required=True,
    opt_type=OptionTypes.STRING,
    description="smallest possible number",
)
@slash_option(
    name="max",
    required=True,
    opt_type=OptionTypes.STRING,
    description="biggest possible number",
)
async def randomise(ctx, num1, num2):
    try:
        await ctx.send(f"> `{num1}` - `{num2}` \n**{random.randint(int(num1), int(num2))}**")
    except:
        await ctx.send("Something didnt go right. Try a different aproach!")


@slash_command(name="calculate", description="calculate some numbers")
@slash_option(
    name="equasion",
    required=True,
    opt_type=OptionTypes.STRING,
    description="input your math equation",
)
async def calculate(ctx, equasion):
    if re.search("[a-z,A-Z]", equasion) is None:
        await ctx.send(
            f"""
> `{equasion}`
**{eval(equasion)}**
        """
        )
    else:
        await ctx.send("Thats not a math equasion...")


# @bot.command(
#     "spotify",
#     description="Share what you're listening to!",
#     options=interactions.Option(
#         name="min",
#         required=True,
#         type=interactions.OptionType.STRING,
#         description="smallest possible number",
#     ),
# )
# async def spotify(ctx: InteractionContext):
#     listener = ctx.author

#     # Get the first activity that contains "Spotify". Return None, if none present.
#     # spotify_activity = next((x for x in listener.activities if x.name == "Spotify"), None)

#     print(listener.activities)

#     if listener.activities[name] == "Spotify":
#         cover = f"https://i.scdn.co/image/{listener.activities.assets.large_image.split(':')[1]}"
#         embed = Embed(
#             title=f"{listener.display_name}'s Spotify",
#             description="Listening to {}".format(listener.activities.details),
#             color="#36b357",
#             thumbnail=cover,
#         )
#         embed.add_field(name="Artist", value=listener.activities.state)
#         embed.add_field(name="Album", value=listener.activities.assets.large_text)
#     else:
#         embed = Embed(
#             title=f"{listener.display_name}'s Spotify",
#             description="Currently not listening to anything",
#             color="#36b357",
#             timestamp=datetime.utcnow(),
#         )
#     embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
#     message = await ctx.send(embeds=embed)
#     await message.add_reaction(spotify_emoji)


# @slash_command("gas", description='"gas-gas-gas" by Manuel')
# async def outro(ctx: InteractionContext):
#     if not ctx.author.voice:
#         return await ctx.send("You are not in a voice channel")
#     else:
#         embed = Embed(
#             'Playing "Gas-gas-gas" by Manuel',
#             description="[Click here to join the voice channel](https://discord.gg/invite/invite)",
#             color="#36b357",
#         )
#         embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
#         await ctx.send(embed=embed)
#         jointhisvc = bot.get_channel(ctx.author.voice.channel)
#         audio = AudioVolume(
#             r"data\gas-gas-gas.mp3",
#         )
#         vc = await jointhisvc.connect(deafened=True)
#         await asyncio.sleep(0.5)
#         await vc.play(audio)
#         await asyncio.sleep(3)
#         await vc.disconnect()

# async def wait_and_kick(member):
#     await asyncio.sleep(27)
#     await member.disconnect()

# @slash_command("outro", description="Exit a voice channel in style")
# async def outro(ctx: InteractionContext):
#     if not ctx.author.voice:
#         return await ctx.send("You are not in a voice channel")
#     else:
#         await ctx.send("You will be disconnected in 25 seconds!", ephemeral=True)
#         jointhisvc = bot.get_channel(ctx.author.voice.channel)
#         audio = AudioVolume(
#             r"data\xenogenesis-outro-song.mp3",
#         )
#         vc = await jointhisvc.connect(deafened=True)
#         await asyncio.sleep(0.5)
#         if __name__ == "__main__":
#             playstuff = await vc.play(audio)
#             playstuff.start()

#             while playstuff.is_alive():
#                 await wait_and_kick()
#         await asyncio.sleep(3)
#         await vc.disconnect()

# @bot.event
# async def on_message(message):
#     channel = message.channel

#     if message.content == "YES":
#         if message.author == owner:
#             await channel.send("Yes indeed")

#     if message.content == "!help":
#         embed = discord.Embed(
#             title="Commands",
#             description="""
# `<message> $` - voting system
# `<message> $<2 - 5>` - voting system with options
# `!quit` - disables bot (emergency use only)
#             """,
#             color=discord.Color.blue(),
#         )

#         await channel.send(embed=embed)

#     if "ratio" in message.content:
#         await message.add_reaction("✅")

#     if message.channel == testsuggestion_channel and message.author != bot.user:
#         await message.add_reaction("⬆️")
#         await message.add_reaction("⬇️")

#     emojiup = "✅"
#     emojidown = "❌"
#     emoji1 = "1️⃣"
#     emoji2 = "2️⃣"
#     emoji3 = "3️⃣"
#     emoji4 = "4️⃣"
#     emoji5 = "5️⃣"
#     if message.content.endswith("$"):
#         await message.add_reaction(emojiup)
#         await message.add_reaction(emojidown)
#     elif message.content.endswith("$2"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#     elif message.content.endswith("$3"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#         await message.add_reaction(emoji3)
#     elif message.content.endswith("$4"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#         await message.add_reaction(emoji3)
#         await message.add_reaction(emoji4)
#     elif message.content.endswith("$5"):
#         await message.add_reaction(emoji1)
#         await message.add_reaction(emoji2)
#         await message.add_reaction(emoji3)
#         await message.add_reaction(emoji4)
#         await message.add_reaction(emoji5)

#     elif message.content == "!quit":
#         if message.author == owner:
#             await channel.send("Logging off...")
#             sleep(1)
#             await bot.change_presence(status=discord.Status.idle)
#             sleep(1)
#             await bot.change_presence(status=discord.Status.offline)
#             await channel.send(f"{bot.user} has logged off")
#             await bot.close()
#             sleep(0.1)
#             print(f"\n{bot.user} has logged out")
#         else:
#             randomnum = randint(0, 8)
#             await channel.send(notauthormessages[randomnum])

#     await bot.process_commands(message)

# @slash_command(
#     name='clear',
#     description='clears messages',

# )
# @Commands.has_permissions(manage_messages=True)
# async def clear(ctx, count):
#     try:
#         await ctx.channel.purge(limit=int(count) + 1)
#     except:
#         await ctx.send("Please input a string!")

# code for floppa friday

secret_TOKEN = os.environ["TOKEN"]
try:
    bot.start(secret_TOKEN)
except Exception as e:
    os.system("kill 1")
    raise Exception(f"Failed to log in, reason: {e}")
