from flask import Flask, render_template, request
import sys
sys.path.append('C:/Users/NEW/Desktop/Aiflaskapp/yugichatbot/Lib/site-packages/')
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot('Candice')
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'My name is Candice'])
trainer.train(['Who are you?', 'I am a bot' ])
trainer.train(['Who created you?', 'Yugesh VP', 'You?'])
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()