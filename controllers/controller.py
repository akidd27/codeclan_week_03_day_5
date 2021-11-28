from app import app
from models.player import Player
from models.game import Game
from flask import render_template, request
from random import choice

result = "No Result"
winner = "None"

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/play')
def play():
    return render_template('play.html', title='Play a Friend')

@app.route('/result', methods=['POST'])
def play_friend():
    player_1 = Player(request.form['player_1_name'], request.form['player_1_choice'])
    player_2 = Player(request.form['player_2_name'], request.form['player_2_choice'])
    game = Game(player_1, player_2)
    winner = game.result()
    if winner:
        result = f"{winner.name} won by playing {winner.choice}!"
    else:
        result = "A draw..."
    return render_template('result.html', title="Result", result=result)

@app.route('/play/computer')
def play_computer():
    return render_template('play_computer.html', title='Play the Computer')

@app.route('/computer/result', methods=['POST'])
def play_computer_result():
    player_1 = Player(request.form['player_1_name'], request.form['player_1_choice'])
    options_list = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(options_list)
    computer_player = Player("The computer", computer_choice)
    game = Game(player_1, computer_player)
    winner = game.result()
    if winner:
        result = f"{winner.name} won by playing {winner.choice}!"
    else:
        result = "A draw..."
    return render_template('computer_result.html', title="Result", result=result)
