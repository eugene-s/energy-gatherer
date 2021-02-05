from celery import Celery

app = Celery('gatherer')

app.config_from_object('gatherer.celeryconfig')
