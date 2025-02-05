from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f'Hello {name}'


@app.route('/f')
@app.route('/f/<temperature>')
def celsius_to_fahrenheit(temperature):
    return f'{float(temperature) * 9 / 5 + 32:.2f}'


if __name__ == '__main__':
    app.run()
