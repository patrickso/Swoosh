import time

from threading import Thread
from flask import Flask, render_template
from flask_ask import Ask, statement
app = Flask(__name__)
ask = Ask(app, '/')


game_info={'game_type':None, 'game_status':'NOGAME'}

def run_classic():
    global game_info
    game_info['game_type']='classic'
    game_info['game_status']='PLAYING'
    start_time = time.time()
    game_info['score'] = 0
    print ("Starting Classic")
    while (time.time()-start_time <60):
        pass
    print ("Ending Classic")
    game_info['game_status']='GAMEOVER'



@ask.intent('PlayClassic')
def play_classic():
    starting_text = 'Starting Classic Game'
    thread = Thread(target = run_classic)
    thread.start()
    return statement(starting_text).simple_card('PlayClassic',starting_text)

@ask.intent('GetScore')
def get_score():
    global game_info
    response_text=''
    if game_info['game_status']=='NOGAME':
        return statement('No game has begun yet')
    if game_info['game_status']=='GAMEOVER':
        response_text='Game Over. '
    if game_info['game_type']=='classic':
        response_text+='Your score is '+str(game_info['score'])
    return statement(response_text)

@ask.intent('GetGameType')
def get_game_type():
    game_type_text=''
    if game_info['game_status']=='NOGAME':
        game_type_text='No game has started yet'
    else:
        game_type_text='You are playing '+game_type
    return statement(game_type_text).simple_card('GetGameType',game_type_text)

if __name__ == '__main__':
    #app.run(ssl_context=('certificate.pem','private-key.pem'),host='0.0.0.0',debug=True)
    app.run(host='0.0.0.0',debug=True)
