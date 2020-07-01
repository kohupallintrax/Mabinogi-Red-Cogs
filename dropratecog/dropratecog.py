import discord
from redbot.core import commands
import math
from typing import Any


class Dropratecog(commands.Cog):
    """Returns expected amount of attempts required to obtain a result given the percentage chance of said event occuring."""

    @commands.command()
    async def droprate(self, ctx: commands.Context, num: float):
        """Returns expected amount of attempts required to obtain a result given the percentage chance of said event occuring. """

        # Check if we were given a decimal of sensible size
        if 100 > float(num):
            #Find the chance of failing - just the inverse of our chance of success
            fail = (1.0 - (num*.01))
            # Find number of attempts to reach 90% threshold. Attempt = desired threshold / fail chance
            attemptCount90 = (math.log(.1)) / (math.log(fail))
            # Find number of attemps to reach 99 percetage threshold
            attemptCount99 = (math.log(.01)) / (math.log(fail))

            msg = "For a success chance of " + str(num) + "% you would need to attempt " + str(round(attemptCount90)) + " times to have a 90 percent chance of having the event occur. For a 99 percent chance of the event occuring you'd need to attempt " + str(round(attemptCount99)) + " times."
        else:
            msg = "Please enter the percent chance of droprate - numbers only please!"

        if await ctx.embed_requested():
            await ctx.send(embed=discord.Embed(description=msg))
        else:
            await ctx.maybe_send_embed(msg)