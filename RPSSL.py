import random
import sqlite3
import flask
import requests
from flask import Flask, request, jsonify

symbol = ["Rock", "Lizard", "Spock", "Scissors", "Paper"]
#1 schlägt 2 usw
def getWinner(a, b):
    if(a == b):return 0
    if((a+1)%(len(symbol)) == b): return 1
    if((a+3)%(len(symbol)) == b): return 1
    return 2

if __name__ == '__main__':
    connection = sqlite3.connect("RPSSL.db", isolation_level=None)
    cursor = connection.cursor()
    cursor.execute("create table if not exists score(name TEXT, score INTEGER)")
    cursor.execute("create table if not exists symbols(symbol TEXT, score INTEGER)")
    with connection:
        q = cursor.execute("select count(*) from score").fetchone()
        if q[0] != 3:
            print("dropping score table")
            cursor.execute("DROP table score")
            cursor.execute("create table if not exists score(name TEXT, score INTEGER)")
            cursor.execute("INSERT INTO score VALUES ('computer', 0)")
            cursor.execute("INSERT INTO score VALUES ('human', 0)")
            cursor.execute("INSERT INTO score VALUES ('draw', 0)")
        q = cursor.execute("select count(*) from symbols").fetchone()
        if q[0] != 5:
            print("dropping symbols table")
            cursor.execute("DROP table symbols")
            cursor.execute("create table if not exists symbols(symbol TEXT, score INTEGER)")
            for i in range(len(symbol)):
                cursor.execute("INSERT INTO symbols VALUES (?, 0)",(symbol[i],))
                print(f"symbol {symbol[i]} added to database")
        score_data = cursor.execute("select * from score").fetchall()
        symbol_data = cursor.execute("select * from symbols").fetchall()

    app = Flask(__name__)
    @app.route('/score')
    def score_serve():
        if (request.method == 'GET'):
            return jsonify({'data': score_data})


    @app.route('/symbols')
    def symbol_serve():
        if (request.method == 'GET'):
            return jsonify({'data': symbol_data})
    app.run()

    player = -1
    for i in range(len(symbol)):
        print(f'{i}: {symbol[i]}')
    player = int(input("Please choose a weapon"))
    while(player == -1 or type(player) != int or player > 4):
        player = int(input("try again"))

    comp = random.randint(0,len(symbol)-1)
    result = getWinner(player, comp)

    print(f'\nPlayer choice: {symbol[player]}')
    print(f'Computer choice {symbol[comp]}')
    if(result == 1):
        print("You won")
        cursor.execute("UPDATE score SET score = score+1 WHERE name=?",("player",))
    elif(result == 2):
        print("Computer won")
        cursor.execute("UPDATE score SET score = score+1 WHERE name=?",("computer",))
    else:
        print("Draw")
        cursor.execute("UPDATE score SET score = score+1 WHERE name=?",("draw",))

    cursor.execute("UPDATE symbols SET score = score+1 WHERE symbol=?", (symbol[player],))
    cursor.execute("UPDATE symbols SET score = score+1 WHERE symbol=?", (symbol[comp],))

