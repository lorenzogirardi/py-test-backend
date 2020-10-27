from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return "main path"

@app.route('/context1', methods=['GET', 'POST'])
def c1():
    return jsonify({'name':'context',
                    'number':'1'})

@app.route('/context2', methods=['GET', 'POST'])
def c2():
    return jsonify({'name':'context',
                    'number':'2'})

@app.route('/context3', methods=['GET', 'POST'])
def c3():
    return jsonify({'name':'context',
                    'number':'3'})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
