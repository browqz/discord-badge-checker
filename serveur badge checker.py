import discord

intents = discord.Intents.default()
intents.members = True

TOKEN = 'MTEzMDkxNjc2MTY0Mjk5NTczMg.GC7E4T.MrBmoMFQ1m21OmfgzvfgX5l7kb0-Axlvs_kHmk'

client = discord.Client(intents=intents)

def get_badges(member):
    badges = []
    flags = member.public_flags

    if flags.early_supporter:
        badges.append('Early Supporter')

    if flags.hypesquad:
        badges.append('HypeSquad Events')

    if flags.bug_hunter:
        badges.append('Bug Hunter')

    if flags.hypesquad_bravery:
        badges.append('HypeSquad Bravery')


    return badges

def bot_loop():
    @client.event
    async def on_ready():
        guild_id = 1168506431964717126

        guild = client.get_guild(guild_id)
        if guild:
            for member in guild.members:
                user_badges = get_badges(member)
                if user_badges:
                    print(f"{member.name} a un : {', '.join(user_badges)}")

    client.run(TOKEN)

if __name__ == "__main__":
    bot_loop()