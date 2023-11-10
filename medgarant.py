import datetime
from datetime import timedelta, datetime

work_day = [
    {'start': '9:00',
     'stop': '21:00'}
]

busy = [
    {'start': '10:30',
     'stop': '10:50'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '14:40',
     'stop': '15:50'},
    {'start': '16:40',
     'stop': '17:20'},
    {'start': '20:05',
     'stop': '20:20'}
]

free = []

busy = sorted(
    busy,
    key=lambda x: datetime.strptime(x['start'], '%H:%M'), reverse=False
)

hours, minutes = map(float, work_day[0]['start'].split(':'))
start_work = timedelta(hours=hours, minutes=minutes)

hours, minutes = map(float, work_day[0]['stop'].split(':'))
stop_work = timedelta(hours=hours, minutes=minutes)

free_window = timedelta(minutes=30)
count = start_work


for t in busy:
    hours_start, minutes_start = map(float, t['start'].split(':'))
    start_bysy = timedelta(hours=hours_start, minutes=minutes_start)

    hours_stop, minutes_stop = map(float, t['stop'].split(':'))
    stop_bysy = timedelta(hours=hours_stop, minutes=minutes_stop)

    while True:
        if count + free_window <= start_bysy:
            free.append(
                {'start': datetime.strptime(str(count), '%H:%M:%S').strftime('%H:%M'),
                 'stop': datetime.strptime(str(count + free_window), '%H:%M:%S').strftime('%H:%M')}
            )
            count += free_window

        else:
            count = stop_bysy
            break

while count + free_window <= stop_work:
    free.append(
        {'start': datetime.strptime(str(count), '%H:%M:%S').strftime('%H:%M'),
         'stop': datetime.strptime(str(count + free_window), '%H:%M:%S').strftime('%H:%M')}
    )
    count += free_window
