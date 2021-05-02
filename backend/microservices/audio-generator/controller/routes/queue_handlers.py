from audio_order import cx_queue, tts_queue
from core.entities import parse_book
from core.usecases import update_audio_order

import time
import threading


class QueuesHandlers:
    __lock = threading.Lock()

    @staticmethod
    def run_queue_handlers():
        def cx_queue_handler():
            while True:
                if cx_queue:
                    QueuesHandlers.__lock.acquire()
                    order_id, sentences = cx_queue[0]
                    cx_queue.popleft()
                    QueuesHandlers.__lock.release()
                    sentences = " ".join(sentences)
                    sentences, chars_names, scripts = parse_book(sentences)
                    update_audio_order(id=id, audio_link=None, chars_names=chars_names, scripts=scripts)
                    ###
                else:
                    time.sleep(60)  # 60 sec

        def tts_queue_handler():
            while True:
                time.sleep(60)
                if tts_queue:
                    QueuesHandlers.__lock.acquire()
                    id, scripts, chars_audios, sentences = tts_queue[0]
                    tts_queue.popleft()
                    QueuesHandlers.__lock.release()
                    if chars_audios is None and scripts is None:
                        #todo: call mozilaa tts
                    else:
                        #todo: call voice cloning


        thread = threading.Thread(target=cx_queue_handler, daemon=True)
        thread.start()
        thread = threading.Thread(target=tts_queue_handler, daemon=True)
        thread.start()