from discord.ext import commands
import discord
import pickle
        
class TravelCog:

    def __init__(self, bot):
        self.bot = bot
        self.HungerAdded = 0.1
        self.ThirstAdded = 0.5

    async def on_message(self,ctx):
        if ctx.message.starts_with('f!'):
            try:
                playerData = pickle.load(open('player.data','rb'))
                playerData[f'{ctx.author.id}']['status']['thirst'] += self.HungerAdded
                playerData[f'{ctx.author.id}']['status']['hunger'] += self.ThirstAdded
                if playerData[f'{ctx.author}']['status']['thirst'] >= 100:
                    await ctx.send("You are about to die fo thirst!")
                if playerData[f'{ctx.author}']['status']['hunger'] >= 100:
                    await ctx.send("You are starving!")
                pickle.dump(playerData,open('player.data','wb'))
            except KeyError:
                return
            

    @commands.command(name='replenish')
    async def Replenish(self,ctx):
        playerData = pickle.load(open('player.data','rb'))
        playerData[f'{ctx.author.id}']['status']['thirst'] = 0
        playerData[f'{ctx.author.id}']['status']['hunger'] = 0
        pickle.dump(playerData,open('player.data','wb'))
        await ctx.send("You hunger and thirst have been sated.")

def setup(bot):
    bot.add_cog(TravelCog(bot))
