import time
from datetime import datetime


def countdown(func):
    def timer():
        for i in range(3, 0, -1):
            print(f'{i}')
            time.sleep(1)
        func()
    return timer


@countdown
def what_time_is_it_now():
    now_time = datetime.now()
    date_str = datetime.strftime(now_time, '%H:%M:%S')
    print(date_str)


what_time_is_it_now()

