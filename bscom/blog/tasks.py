from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

# from baseline.queue.celery import app


@shared_task
def import_drafts_from_dropbox():
    with open("/home/brant/task.log", "a") as f:
        f.write("Updated... %s" % datetime.now())
