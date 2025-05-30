import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get keys from .env (using same naming convention as your working FastAPI app)
GENAI_API_KEY = os.getenv('GENAI_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Validate API keys
if not GENAI_API_KEY:
    raise ValueError("GENAI_API_KEY not found in environment variables")

if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN not found in environment variables")

# Configure Gemini API (same as your working FastAPI app)
genai.configure(api_key=GENAI_API_KEY)

# Discord setup
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def AI(ctx):
    question = ctx.message.content[4:].strip()
    
    if not question:
        await ctx.send("❗ Please provide a question after the !AI command.")
        return
    
    try:
        # Use the same model as your working FastAPI app
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(question)
        
        # Discord has a 2000 character limit for messages
        response_text = response.text
        if len(response_text) > 2000:
            # Split long responses
            for i in range(0, len(response_text), 2000):
                await ctx.send(response_text[i:i+2000])
        else:
            await ctx.send(response_text)
            
    except Exception as e:
        print(f"Gemini API Error: {e}")
        await ctx.send(f"⚠️ Gemini API Error: {str(e)}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN, log_handler=handler, log_level=logging.DEBUG)