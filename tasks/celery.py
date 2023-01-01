from celery import Celery
from datetime import timedelta
# from celery.schedules import crontab

app = Celery(
    'tasks',
    #  broker='redis://127.0.0.1:6379', # для локального селери
    #  backend='redis://127.0.0.1:6379',
     broker='redis://redis:6379', # для контейнера
     backend='redis://redis:6379',
     include=['tasks.tasks']
)

app.conf.beat_schedule = {
    'tmp-beat': {
        'task': 'tasks.tasks.add',
        'options': {'queue' : 'celery_periodic'},
        # 'schedule': crontab(minute='*/1'),
        'schedule': timedelta(seconds=10),
        'args': (16, 16),
    },
}

if __name__ == '__main__':
    app.start()