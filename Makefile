run:
	uvicorn main:app --reload
celery:
	celery -A tasks.tasks.celery_app worker --loglevel=info
flower:
	celery -A tasks.tasks.celery_app flower --port=5555
