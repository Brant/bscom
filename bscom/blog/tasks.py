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
    with open("/home/brant/bscom16/task.log", "a") as f:
        f.write("Updated... %s\n" % datetime.now())
        f.write("%s\n" % request.body)

        f.write("%s\n" % request.META['HTTP_X_DROPBOX_SIGNATURE'])

        message = bytes(request.body).encode('utf-8')
        secret = bytes(settings.DROPBOX_SECRET).encode('utf-8')

        signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest())
        f.write("%s\n" % signature)

