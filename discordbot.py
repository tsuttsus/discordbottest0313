from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def poll(ctx, about = "question", *args):
    emojis = ["1⃣","2⃣","3⃣","4⃣"]

    cnt = len(args)
    message = discord.Embed(title=":speech_balloon: "+about,colour=0x1e90ff)
    if cnt <= len(emojis):
        for a in range(cnt):
            message.add_field(name=f'{emojis[a]}{args[a]}', value="** **", inline=False)
        msg = await ctx.send(embed=message)
        #投票の欄
        for i in range(cnt):
            await msg.add_reaction(emojis[i])
    else:
        await ctx.send("項目は4つまでなんだ...")

'''
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
'''
bot.run(token)
