import sys
from os import path
from controller import app

sys.path.append(path.join(path.realpath(__file__), '..'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)
