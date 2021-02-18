# speaking clock app

from datetime import datetime
import time
import os
import schedule


# job define
def job_say_time():
    time_str = datetime.now().strftime('Il est %H heures %M minutes %S secondes')
    time_str = time_str.lstrip('0').replace(' 0', ' ')
    cmd = '{ espeak -v mb-fr1 -s 95 \'%s.\' --stdout | aplay; } >/dev/null 2>&1' % time_str
    print('run command: %s' % cmd)
    os.system(cmd)


# schedule job call
schedule.every().minute.at(':00').do(job_say_time)
schedule.every().minute.at(':15').do(job_say_time)
schedule.every().minute.at(':30').do(job_say_time)
schedule.every().minute.at(':45').do(job_say_time)

# main loop
while True:
    schedule.run_pending()
    idle_s = schedule.idle_seconds()
    if idle_s is None:
        break
    elif idle_s > 0:
        time.sleep(idle_s)
