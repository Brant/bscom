from datetime import datetime
import hmac
import hashlib
import base64

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

# from baseline.queue.celery import app


@shared_task
def import_drafts_from_dropbox(request):
    with open("/home/brant/task.log", "a") as f:
        f.write("Updated... %s\n" % datetime.now())
        f.write("%s" % request.body)
        # f.write("%s" % request.META)
        f.write("%s" % request.META['HTTP_X_DROPBOX_SIGNATURE'])
        dig = hmac.new(settings.DROPBOX_SECRET, msg=request.body, digestmod=hashlib.sha256).digest()
        f.write("%s" % dig)
        # base64.b64encode(dig).decode()
