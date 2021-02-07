import discord
import os
import requests
import json
import re
import random
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragement = ["Cheer up!", "Hang in there.", "You are a great person"]

def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " - " + json_data[0]['a']
	return(quote)

@client.event

async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	
@client.event

async def on_message(message):

	if message.author == client.user:
		return

	if re.search("^hi",message.content,re.IGNORECASE):
		  await message.channel.send('Hello '+str(message.author)+'!')

	if re.search("^inspire",message.content,re.IGNORECASE):
		quote = get_quote()
		await message.channel.send(quote)

	if any(word in message.content for word in sad_words):
		await message.channel.send(random.choice(starter_encouragement))

keep_alive()
client.run(os.getenv('TOKEN'))