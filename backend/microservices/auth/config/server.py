import os


SECRET_KEY_LENGTH = 32
SERVER_EMAIL = 'smtp.gmail.com'
SERVER_EMAIL_PORT = 465
SERVER_EMAIL_USERNAME = 'bookbeat.project@gmail.com'
SERVER_EMAIL_PASSWORD = '8_R75a</V^Ew**/L^c~C'


JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES = int(os.environ.get('JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES')) \
    if 'JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES' in os.environ else 15
JWT_REFRESH_TOKEN_LIFETIME_IN_MINUTES = int(os.environ.get('JWT_REFRESH_TOKEN_LIFETIME_IN_MINUTES')) \
    if 'JWT_REFRESH_TOKEN_LIFETIME_IN_MINUTES' in os.environ else 60 * 24
