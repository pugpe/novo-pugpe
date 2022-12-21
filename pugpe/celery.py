import os

from celery import Celery
from django.core import management

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pugpe.settings")

app = Celery("pugpe")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
