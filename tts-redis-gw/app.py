# tts redis gateway app

from datetime import datetime
import os
from shlex import quote
import time
import traceback
import redis
import logging


# TTS processing (send txt string to espeak/mbrola engine for speech job)
def tts(txt):
    # send blank before speak (workaround for avoid losing beginig of txt)
    os.system('{ espeak -v mb-fr1 -s 95 "" --stdout | aplay; } >/dev/null 2>&1')
    # send txt to espeak
    cmd = '{ espeak -v mb-fr1 -s 95 %s --stdout | aplay; } >/dev/null 2>&1' % quote(
        txt)
    logging.debug('run command: %s' % cmd)
    os.system(cmd)


if __name__ == '__main__':
    # logging setup
    logging.basicConfig(format='%(levelname)s\t%(message)s',
                        level=logging.WARNING)
    # main loop
    while True:
        try:
            # subscribe to redis publish channel
            r = redis.StrictRedis(
                host='redis-srv', socket_connect_timeout=4, socket_keepalive=True)
            ps = r.pubsub()
            ps.subscribe(['tts-channel'])

            # wait for email to send
            for item in ps.listen():
                if item["type"] == "message":
                    try:
                        tts(item["data"].decode())
                    except:
                        logging.warning(traceback.format_exc())
        except redis.RedisError:
            logging.warning(traceback.format_exc())
            time.sleep(10)
        except:
            logging.error(traceback.format_exc())
            break
