import discord
import asyncio
import random
from redbot.core import commands, checks

class Rand(commands.Cog):
    """
    Simple random cog
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=3, type= commands.BucketType.user)
    async def sendmessage(self, ctx: commands.Context, *, text: str = ""):
        """this command sends a message"""
        if text == "":
            message = "there is no text"
        else:
            message = text
        await ctx.send(message)

    @commands.command(name="react")
    @commands.cooldown(rate=1, per=3, type= commands.BucketType.user)
    async def reaction(self, ctx: commands.Context, msg_id: int, emoji = None, channel: discord.TextChannel = None):
        """react to a message.\n
        msg_id is the message id you want to react to.\n
        emoji is a emoji.\n
        channel is a channel"""
        if not channel:
            channel  = ctx.channel
        if not emoji:
            emoji = "✅"
        try:
            msg = await channel.fetch_message(msg_id)
            await msg.add_reaction(emoji)
        except discord.HTTPException:
            await ctx.send("that message id isn't in this channel please specify the channel the message is in or use the correct message id.")
     
    @commands.command(name="pls")
    @commands.cooldown(rate=1, per=3, type= commands.BucketType.user)
    async def pornhub(self, ctx: commands.Context, *, text: str = ""):
        """this will send a message"""
        if text == "":
            message = "please use right command or say something after the command."
        elif text == "help":
            message = "im stuck stepbro"
        else: 
            message = "thats fifty p fuck you bastard"
        await ctx.send(message)
          
    @commands.command(name="isalexhot")
    @command.cooldown(rate=1, per=3, type= commands.BucketType.user)
    async def randomizer(self, ctx: commands.Context):
       """this command sends a message"""
       a = random.randint(1, 2)
       if a == 1:
         message = "even hotter than your Nan"
       elif a == 2:
         message = "he is so hot hes melting the Sun"
       await ctx.send(message)
        
        


    
    
