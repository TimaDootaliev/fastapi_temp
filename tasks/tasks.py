from celery import Celery

from core.settings import settings


celery_app = Celery(
    'tasks',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=['tasks.tasks']
)


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def divide(x, y):
    return x / y
