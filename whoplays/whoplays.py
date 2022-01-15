import discord

from redbot.core.bot import Red
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS

import operator 


class WhoPlays(commands.Cog):
    """
    shows who plays what
    """
    
    __author__ = ["jari", "wulf"]
    __version__ = "1.0.0"
    
    def __init__(self, bot: Red):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nVersion: {self._version__}"

    @commands.command()
    @commands.guild_only()
    async def whoplays(self, ctx: command.Context, *, game: str):
        """shows who plays what"""
        if len(game) <= 2:
            await ctx.send("you need atleast 3 characters.")
            return

        member_list = []
        count_playing = 0
        for member in ctx.guild.members:
            if not member:
                continue
            if not member.activity or not member.activity.name:
                continue
            if member.bot:
                continue
            if activity := discord.utils.get(member.activities, type= discord.ActivityType.playing):
                if game.lower() in activity.name.lower():
                    member_list.append(member)
                    count_playing += 1

        if count_playing == 0:
            await ctx.send("no one is playing that game.")
        else:
            sorted_list = sorted(member_list, key=lambda x: getattr(x, "name").lower())
            playing_game = ""
            for member in sorted_list:
                playing_game += "▸ {} ({})\n".format(member.name, member.activity.name)
            embed_list = []
            in_pg_count = 0

            for page in pagify(playing_game, delims=["\n"], page_length=400):
                in_page = page.count("▸")
                in_pg_count = in_pg_count + in_page
                title = f"these are the people who are playing {game}:\n"
                em = discord.Embed(discription=page, colour=ctx.author.colour)
                em.set_footer(text=f"showing {in_pg_count}/{count_playing}")
                em.set_author(name=title)

            if len(embed_list) == 1:
                return await ctx.send(embed=em)
            await menu(ctx, embed_list, DEFAULT_CONTROLS)
            
            
            
           
        