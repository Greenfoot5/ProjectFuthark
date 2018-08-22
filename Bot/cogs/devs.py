from discord.ext import commands
import discord
import pickle
        
class DevCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='dev', aliases='d')
    async def dev(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcomand sent.")
    
    # Hidden means it won't show up on the default help.
    @dev.command(name='load', hidden=True)
    @commands.has_any_role('Developer')
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @dev.command(name='unload', hidden=True)
    @commands.has_any_role('Developer')
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @dev.command(name='reload', hidden=True)
    @commands.has_any_role('Developer')
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @dev.command(name='embeds')
    @commands.has_any_role('Developer')
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.

        Have a play around and visit the Visualizer."""

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)

    #Adds a spacer to the console.
    @dev.command('spacer')
    @commands.has_any_role('Developer')
    async def Spacer(self,ctx):
        print("--------------------------------------------------")

    #Basic stats layout. Showing Tito how embeds work.
    @dev.command('test')
    @commands.has_any_role('Developer')
    async def Test(self,ctx):
        embed = discord.Embed(title=ctx.author.display_name,
                              description=f"{ctx.author.mention}'s stats",
                              colour=0x008800)
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar_url_as(format='png'))
        #embed.set_image(url='https://i.imgur.com/5BFecvA.png')
        embed.set_thumbnail(url=ctx.author.avatar_url_as(format='png'))

        embed.add_field(name='Balance',value=5,inline=False)
        embed.add_field(name='Wins',value=25)
        embed.add_field(name='Loses',value=0)
        
        embed.set_footer(text=ctx.guild.name,
                         icon_url=ctx.guild.icon_url_as(format='png'))
        await ctx.send(content='Message',embed=embed)

    @dev.command(name='register')
    @commands.has_any_role('Developer')
    async def MemberRegister(self,ctx):
        embed = discord.Embed(title='Register!?',
                              description="I have told you already! The Gods have deemed the world not ready. When the time comes simply ask in #gate and you should be permitted! Now, please don't pseter me! I like my peace and quiet. I don't get much when the gates open.",
                              colour=0x666666)
        embed.set_author(name='Gate Keeper',
                         icon_url='')
        #embed.set_thumbnail(url=ctx.author.avatar_url_as(format='png'))

        embed.add_field(name='When will they open?',value='You will know when it is ready.')
        
        embed.set_footer(text=self.bot.get_guild(476728702131109888).name,
                         icon_url=self.bot.get_guild(476728702131109888).icon_url_as(format='png'))
        await ctx.send(content='',embed=embed)

def setup(bot):
    bot.add_cog(DevCog(bot))
