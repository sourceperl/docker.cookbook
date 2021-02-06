# python simple app

import schedule
from datetime import datetime as dt
import time


def job():
    iso_str = dt.now().astimezone().replace(microsecond=0).isoformat()
    print('Hello from py-simple-app [container time is %s]' % iso_str)


if __name__ == '__main__':
    # schedule setup
    schedule.every(5).seconds.do(job)
    # first run now
    job()
    # main loop
    while True:
        schedule.run_pending()
        time.sleep(0.5)
