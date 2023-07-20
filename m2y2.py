import os, random
import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

facts = ["Не повреждать и не рвать без нужды растения", "не ломать ветки", "Не шуметь, не включать громкую музыку", 
         "Не кормить диких животных", "Не трогать птиц, насекомых", 
         "Не оставлять надписи на камнях и прочих природных объектах", "Для разведения костра использовать старые кострища", 
         "Ненужный костер затушить и засыпать землей", "Не разводить костры там, где это запрещено", 
         "Не использовать на природе бытовую химию", "Закапывать органические отходы"]

@bot.command('help-bot')
async def help_bot(ctx):
    await ctx.send("Команды и их обозначения")
    await ctx.send("fact - выводит случайный экологический факт")

@bot.command('fact')
async def fact(ctx):
    random_fact = random.choice(facts)
    await ctx.send(random_fact)

token = "MTEyNzkzODg4NTI1NTcwODY5Mg.G7uBRz.gDe9-tIGaVbOo_pc6_zJSM8sW0Qnw_iFHWtgak"
bot.run(token)