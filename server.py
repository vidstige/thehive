
import random
from flask import Flask, jsonify, render_template
import hive

app = Flask(__name__)

# debug hax
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

state = None

@app.route('/')
def hello_world():
    return render_template('index.html')

def state2dict(state):
    return {
        'grid': {repr(c): repr(v[0]) for c, v in state.grid.items()}
    }

@app.route('/api/state')
def get_state():
    if not state:
        return jsonify(None)
    return jsonify(state2dict(state))

@app.route('/api/random')
def random_move():
    the_moves = list(hive.available_moves(state))
    if not the_moves:
        return "No available moves"
    move = random.choice(the_moves)
    state.do(move)

    return jsonify("OK")