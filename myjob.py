from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('定时任务： %s' % datetime.now())



if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    # scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.add_job(tick, 'cron', second=5)

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass