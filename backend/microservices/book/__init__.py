from core.entities.make_book import build_make_book
from core.entities.make_user_book import build_make_user_book

from controller import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)