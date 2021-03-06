from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/suman/OneDrive/Desktop/Chatbot project/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data = open('C:/Users/suman/OneDrive/Desktop/Chatbot project/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
	bot.train(data)
while True:
	message = input('You: ')
	if message.strip != 'Bye':
		reply = bot.get_response(message)
		print('Chatbot: ',reply)
	if message.strip() == 'Bye':
		print('Chatbot: Bye')
		break