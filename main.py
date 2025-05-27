import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def AI(ctx):
    
    # Configure Gemi
    # Get the user's question (everything after !AI)
    question = ctx.message.content[4:].strip()
    
    if not question:
        await ctx.send("Please provide a question after the !AI command")
        return

    try:
        # Generate response from Gemini
        response = model.generate_content(question)
        
        # Send response back to Discord
        await ctx.send(response.text)
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error: {str(e)}")
bot.run(token, log_handler=handler, log_level=logging.DEBUG)