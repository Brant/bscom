from datetime import datetime
import hmac
import hashlib
import base64
import dropbox

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

# from baseline.queue.celery import app


@shared_task
def import_drafts_from_dropbox(request):
    with open("/home/brant/bscom16/task.log", "a") as f:
        f.write("Updated... %s\n" % datetime.now())
        # f.write("%s\n" % request.body)

        # f.write("%s\n" % request.META['HTTP_X_DROPBOX_SIGNATURE'])

        signature = hmac.new(settings.DROPBOX_SECRET, request.body, digestmod=hashlib.sha256).hexdigest()
        # f.write("%s\n" % signature)

        client = dropbox.client.DropboxClient(settings.DROPBOX_TOKEN)
        f.write("%s\n" % client.metadata(settings.DROPBOX_DRAFTS_PATH))
