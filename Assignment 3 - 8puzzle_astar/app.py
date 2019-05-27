from flask import Flask, render_template, jsonify
import apuzzle as p
import time

apuzzle = Flask(__name__)

@apuzzle.route('/', methods=['GET'])
def main():
    p.init()
    initial = p.initial_state
    starttime = time.time()
    astar= p.a_star(initial)
    astartime = round(time.time()-starttime, 2)
    moves = p.backtrace2()
    starttime = time.time()
    bfs= p.bfs(initial)
    bfstime = round(time.time()-starttime, 2)
    moves2 = p.backtrace()
    return render_template('index.html', initial=initial, moves=moves,astartime=astartime, bfstime=bfstime, moves2=moves2,astar=astar,bfs=bfs)

apuzzle.run(debug=True)