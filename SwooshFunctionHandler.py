import time

from threading import Thread
from flask import Flask, render_template
from flask_ask import Ask, statement
app = Flask(__name__)
ask = Ask(app, '/')

global game_type
score_list=[]
game_type=None

def run_classic():
    game_type='classic'
    start_time = time.time()
    score_list.append(0)
    while (time.time()-start_time <60):
        pass
    game_type=None



@ask.intent('PlayClassic')
def play_classic():
    starting_text = 'Starting Classic Game'
    thread = Thread(target = run_classic)
    thread.start()
    return statement(starting_text).simple_card('PlayClassic',starting_text)

@ask.intent('GetScore')
def get_score():
    text = 'getting score'
    return statement(text).simple_card('Hello', text)

@ask.intent('GetGameType')
def get_game_type():
    game_type_text=''
    if game_type==None:
        game_type_text='No game has started yet'
    else:
        game_type_text='You are playing '+game_type
    return statement(game_type_text).simple_card('GetGameType',game_type_text)

if __name__ == '__main__':
    #app.run(ssl_context=('certificate.pem','private-key.pem'),host='0.0.0.0',debug=True)
    app.run(host='0.0.0.0',debug=True)
