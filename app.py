from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name/<name>')
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
