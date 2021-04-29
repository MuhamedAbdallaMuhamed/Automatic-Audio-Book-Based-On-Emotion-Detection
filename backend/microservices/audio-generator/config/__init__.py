from .audioOrder import *
from .server import *
from .serviceCredential import *

import os
APP_PATH = os.path.abspath('.')

if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/serviceAccountKey.json'
