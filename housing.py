# base URL for housing search 208.85.109.181/MabinogiShopAdv/ShopAdvertise.asp?Name_Server=mabius3&CharacterId=4503599627432536&Page=1&Row=7&SearchType=4&SortType=5&SortOption=1&SearchWord=
# Require lxml

import discord
from discord.ext import commands
import aiohttp
import requests
from xml.etree import ElementTree

class Housing:
    """Mabinogi housing search cog"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def housing(self, search):
        """Search mabinogi housing"""
        #Your code will go here
        url = ("http://208.85.109.181/MabinogiShopAdv/ShopAdvertise.asp?Name_Server=mabius3&CharacterId=4503599627432536&Page=1&Row=7&SearchType=4&SortType=5&SortOption=1&SearchWord=" + search) #build the web adress
        response = requests.get(url)
        root = ElementTree.fromstring(response.content)
        try:
            charNameList = []
            itemNameList = []
            itemPriceList = []
            housingList = []
            msg = ""
            for child in root.findall('ItemDesc'):
                charName = child.get('Char_Name')
                itemName = child.get('Item_Name')
                itemPrice = int(child.get('Item_Price'))
                housingList.append([charName, itemName, itemPrice])
            for charName, itemName, itemPrice in housingList:
                msg += "[Seller]: "+ charName + " [Item:] " + itemName + " [Price]: " + '{0:,}'.format(itemPrice) +  "\n\n"
            await self.bot.say(msg)
        except:
            await self.bot.say("Couldn't search housing. No results or there was an error.")
    
     


def setup(bot):
    bot.add_cog(Housing(bot))