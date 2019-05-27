from flask import Flask, render_template, jsonify
import bfspuzzle as p

bfspuzzle = Flask(__name__)

@bfspuzzle.route('/', methods=['GET'])
def main():
    p.init()
    initial = p.initial_state
    p.bfs(initial)
    moves = p.backtrace()
    return render_template('index.html', initial=initial, moves=moves)

bfspuzzle.run(debug=True)