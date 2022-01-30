import discord #import all the necessary modules
from neuralintents import GenericAssistant
import requests
def get_price():

    url = 'https://api.tinychart.org/asset/452399768/price'
    json = requests.get(url, params = None , headers = {
        'x-api-key': 'iy3O5Dxb6C5yTD5J7xro83nrv2jvdFShcds081n2',
        'Accepts' : 'application/json'
    } ).json()
    price = json.get('price')
    return price


chatbot = GenericAssistant('intents2.json')
chatbot.train_model()
chatbot.save_model()

print('bot done training')



client = discord.Client()
#price1 = get_price()
@client.event 
async def on_message(message):
    if message.author == client.user:
        return

        
    if message.content.startswith("Bot"):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

    if message.content.startswith("!"):
        response = chatbot.request(message.content[1:])
        price = get_price()
        await message.channel.send("the current price is " + str(price))

client.run('OTI3NTI3MTE3NzMyODY4MTY2.YdLg8Q.FDRPHDZrIewUhWemEjOhW2b9C-E')
