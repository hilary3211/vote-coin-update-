import discord #import all the necessary modules
from neuralintents import GenericAssistant
import requests
def vote_usdc():

    url = ' https://api.vote-coin.com/Price/Get/31566704/452399768'
    json = requests.get(url).json()
    price = json
    return price


def vote_algo():

    url = 'https://api.vote-coin.com/Price/Get/0/452399768'
    json = requests.get(url).json()
    price = json
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
        price = vote_usdc()
        await message.channel.send("the current price is " + str(price))

    if message.content.startswith("?"):
        response = chatbot.request(message.content[1:])
        price = vote_algo()
        await message.channel.send("the current price is " + str(price))

client.run('OTI3NTI3MTE3NzMyODY4MTY2.YdLg8Q.pKMdq9SU5mcSKXafLCFlRQIdSg0')
