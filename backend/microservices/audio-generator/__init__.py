import sys
from os import path
sys.path.append(path.join(path.realpath(__file__), '..'))
from controller import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
