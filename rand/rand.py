import discord
import asyncio
import random
from redbot.core import commands, checks
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from redbot.core.utils.chat_formatting import pagify

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
    @commands.cooldown(rate=1, per=3, type= commands.BucketType.user)
    async def randomizer(self, ctx: commands.Context):
       """this command sends a message"""
       a = random.randint(1, 2)
       if a == 1:
         message = "even hotter than your Nan"
       elif a == 2:
         message = "he is so hot hes melting the Sun"
       await ctx.send(message)
    
    @commands.command(name="embed")
    async def embed(self, ctx: commands.Context):
        """sends embed"""
        embeds = []
        embed= discord.Embed(title="nice cock bro", url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5MrUhHgBnfaer3Gqjd-T8inZuN3Ylli5pYQ&usqp=CAU", description="damn thats at least 2 inches", color=0x079de9)
        embed.set_author(name="WeirdChamp", url="https://media.makeameme.org/created/nice-cock-bro-bf0ac0330e.jpg", icon_url="https://media.makeameme.org/created/nice-cock-bro-bf0ac0330e.jpg")
        embed.set_thumbnail(url="https://media.makeameme.org/created/nice-cock-bro-bf0ac0330e.jpg")
        embed.set_image(url="https://media.makeameme.org/created/nice-cock-bro-bf0ac0330e.jpg")
        embed.add_field(name="nice cock generator", value="https://xngay.com/wp-content/uploads/2019/12/%F0%9F%91%85%F0%9F%91%85%F0%9F%91%853-1.jpg", inline=True)
        embed.add_field(name="nice cock generator", value="https://media.makeameme.org/created/nice-cock-bro-bf0ac0330e.jpg", inline=True)
        embed.set_footer(text="big ass cock")
        embeds.append(embed)
        
        picture = "http://thematuresluts.com/pictures/galleries/4/048/0_147.jpg"
        embed= discord.Embed(title="hot Nan", url=f"{picture}", description="damn nice tits", color=0x079de9)
        embed.set_author(name="WeirdChamp", url=f"{picture}", icon_url=f"{picture}")
        embed.set_thumbnail(url=f"{picture}")
        embed.set_image(url=f"{picture}")
        embed.add_field(name="nice cock generator", value=f"{picture}", inline=True)
        embed.add_field(name="nice cock generator", value=f"{picture}", inline=True)
        embed.set_footer(text="big nana milkers")
        embeds.append(embed)
        await menu(ctx, pages=embeds, controls=DEFAULT_CONTROLS, message=None, page=0, timeout=180)
        
        


    
    
