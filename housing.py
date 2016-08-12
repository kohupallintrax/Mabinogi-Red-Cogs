import discord
from discord.ext import commands
import requests
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

class Housing:
    """Mabinogi housing search cog"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def housing(self, search):
        """Search mabinogi housing"""
        #Build the web address, hit the webpage then retrieve and parse the XML
        url = ("http://208.85.109.181/MabinogiShopAdv/ShopAdvertise.asp?Name_Server=mabius3&CharacterId=4503599627432536&Page=1&Row=7&SearchType=4&SortType=5&SortOption=1&SearchWord=" + search) 
        response = requests.get(url)
        
        #Grab relevant attributes from the XML for Seller, Item and Price
        try:
            root = ElementTree.fromstring(response.content)
            charNameList = []
            itemNameList = []
            itemPriceList = []
            housingList = []
            msg = ""
            #Iterate through the XML file for each item hit and append it to the housing list. Price needs          to be an integer
            for child in root.findall('ItemDesc'):
                charName = child.get('Char_Name')
                itemName = child.get('Item_Name')
                itemPrice = int(child.get('Item_Price'))
                housingList.append([charName, itemName, itemPrice])
            #Construct the message our bot will say. Its ugly because I suck at programming. Would have done it the Python way but I wanted  commas in the price and didn't want to think ;)    
            for charName, itemName, itemPrice in housingList:
                msg += "[Seller]: "+ charName + " [Item]: " + itemName + " [Price]: " + '{0:,}'.format(itemPrice) +  "\n\n"
            await self.bot.say(msg)
        except ElementTree.ParseError:
            await self.bot.say("There were no results or there was an error.")
    
     


def setup(bot):
    bot.add_cog(Housing(bot))