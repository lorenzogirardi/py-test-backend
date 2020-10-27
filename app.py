from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "main path"

@app.route('/context1')
def c1():
    return "context 1"

@app.route('/context2')
def c2():
    return "context 2"

@app.route('/context3')
def c3():
    return "context 3"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

