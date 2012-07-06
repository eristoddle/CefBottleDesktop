import sys
sys.path.append("./lib/bottle")

import os
from bottle import route, run

def RunBottle():
    run(host='localhost', port=800)

@route('/hello/<name>')
def index(name='World'):
    welcome = '<b>Hello %s!</b>' % name
    return welcome + '<br/><a href="/pid/">pid</a>'

@route('/pid/')
def pid():
    return str(os.getpid())

if __name__ == "__main__":
    RunBottle()