from config import *

import time
import threading


class TokenDb:
    __BLOCKED_TOKENS_1 = set()
    __BLOCKED_TOKENS_2 = set()
    __ACTIVE_BLOCKED_TOKENS = __BLOCKED_TOKENS_1
    __lock = threading.Lock()

    @staticmethod
    def insert_token(token: str):
        TokenDb.__ACTIVE_BLOCKED_TOKENS.add(token)
        return True

    @staticmethod
    def is_token_exist(token: str):
        return token in TokenDb.__BLOCKED_TOKENS_1 or token in TokenDb.__BLOCKED_TOKENS_2

    # this method should run every access_token_lifetime
    @staticmethod
    def __clear_tokens():
        TokenDb.__lock.acquire()
        if TokenDb.__ACTIVE_BLOCKED_TOKENS is TokenDb.__BLOCKED_TOKENS_1:
            TokenDb.__BLOCKED_TOKENS_2.clear()
            TokenDb.__ACTIVE_BLOCKED_TOKENS = TokenDb.__BLOCKED_TOKENS_2
        else:
            TokenDb.__BLOCKED_TOKENS_1.clear()
            TokenDb.__ACTIVE_BLOCKED_TOKENS = TokenDb.__BLOCKED_TOKENS_1
        TokenDb.__lock.release()

    @staticmethod
    def run_clear_tokens_job():
        def clear_token_thread():
            while True:
                time.sleep(JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES * 60)
                TokenDb.__clear_tokens()

        thread = threading.Thread(target=clear_token_thread, daemon=True)
        thread.start()
