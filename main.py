# import packages
import discord
import os
import requests
import json
import random
# Instance of a client-Connection to discord
client = discord.Client()

sad_words= ["sad","depressed","unhappy","angry","miserable","depressing"]

encouragements=["Cheer Up!","You are too good","Be Motivated!"]
def get_quote():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote="''"+json_data[0]['q']+"''"+"-"+json_data[0]['a']
  return(quote)
# register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$inspire'):
      quote=get_quote()
      await message.channel.send(quote)

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(encouragements))

client.run(os.getenv('TOKEN'))
