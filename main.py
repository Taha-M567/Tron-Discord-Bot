import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import google.generativeai as genai
import json

# Load environment variables
load_dotenv()

with open('course_data.json', 'r', encoding='utf-8') as f:
    course_data = json.load(f)
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

# def search_course_data(question):
#     q = question.lower()
#     # Try to match aliases
#     for dicts in course_data.get("course_aliases", []):
#         for dict in dicts:
#             alias = dict.get("aliases", [])
#             if alias in q:
#                 for course in course_data.get("courses", []):
#                     if course.get("name", "").lower() == code.lower():
#                         # Find professor for this course
#                         for prof in course_data.get("professors", []):
#                             if code in prof.get("courses", []):
#                                 info = f"Professor: {prof['name']}\nEmail: {prof.get('email', 'N/A')}\nOffice: {prof.get('office', 'N/A')}"
#                                 if "office_hours" in prof:
#                                     info += f"\nOffice Hours: {prof['office_hours']}"
#                                 return info
#     # Fallback to original logic
#     for course in course_data.get("courses", []):
#         if course.get("name") and course["name"].lower() in q:
#             return f"Course: {course.get('full_name', '')}\nDescription: {course.get('description', '')}\nUnits: {course.get('units', '')}"
#     for prof in course_data.get("professors", []):
#         if prof.get("name") and prof["name"].lower() in q:
#             info = f"Professor: {prof['name']}\nEmail: {prof.get('email', 'N/A')}\nOffice: {prof.get('office', 'N/A')}"
#             if "office_hours" in prof:
#                 info += f"\nOffice Hours: {prof['office_hours']}"
#             return info
#     for ta in course_data.get("teaching_assistants", []):
#         if ta.get("name") and ta["name"].lower() in q:
#             return f"TA: {ta['name']}\nEmail: {ta.get('email', 'N/A')}\nCourses: {', '.join(ta.get('courses', []))}"
#     return None
def search_course_data(question):
    q = question.lower()

    # Step 1: Match the question to a course name via its aliases
    matched_course_code = None
    for entry in course_data.get("course_aliases", []):
        aliases = entry.get("aliases", [])
        course_name = entry.get("name", "").lower()
        for alias in aliases:
            if alias.lower() in q:
                matched_course_code = course_name
                break
        if matched_course_code:
            break

    # Step 2: If a course match is found, find the corresponding professor
    if matched_course_code:
        for prof in course_data.get("professors", []):
            if matched_course_code.upper() in prof.get("courses", []):
                info = f"Professor: {prof['name']}\nEmail: {prof.get('email', 'N/A')}\nOffice: {prof.get('office', 'N/A')}"
                if "office_hours" in prof:
                    info += f"\nOffice Hours: {prof['office_hours']}"
                return info

    # Step 3: Fallback – nothing found
    return None
@bot.command()
async def AI(ctx):
    question = ctx.message.content[4:].strip()

    if not question:
        await ctx.send("❗ Please provide a question after the !AI command.")
        return

    # First, try to answer from the JSON file
    json_answer = search_course_data(question)
    if json_answer:
        await ctx.send(json_answer[:2000])
        return

    try:
        # Use Gemini if no answer found in JSON
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(question)
        response_text = response.text
        if len(response_text) > 2000:
            for i in range(0, len(response_text), 2000):
                await ctx.send(response_text[i:i+2000])
        else:
            await ctx.send(response_text)
    except Exception as e:
        print(f"Gemini API Error: {e}")
        await ctx.send(f"⚠️ Gemini API Error: {str(e)}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN, log_handler=handler, log_level=logging.DEBUG)