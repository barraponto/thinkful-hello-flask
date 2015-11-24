from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def say_hi():
    return 'Hello World!'

@app.route('/hello/<name>')
def hi_person(name):
    return 'Hello {}!'.format(name.title())

@app.route('/jedi/<first_name>/<last_name>')
def hi_jedi(first_name, last_name):
    return '{}-{}'.format(last_name[:3], first_name[:2])

if __name__ == '__main__':
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
