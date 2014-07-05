from __future__ import absolute_import

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
        # f.write("Updated... %s\n" % datetime.now())
        # f.write("%s\n" % request.body)

        # f.write("%s\n" % request.META['HTTP_X_DROPBOX_SIGNATURE'])

        signature = hmac.new(settings.DROPBOX_SECRET, request.body, digestmod=hashlib.sha256).hexdigest()
        if request.META['HTTP_X_DROPBOX_SIGNATURE'] == signature:
            f.write("Updated... %s\n" % datetime.now())
        # f.write("%s\n" % signature)

        # client = dropbox.client.DropboxClient(settings.DROPBOX_TOKEN)
        # has_more = True

        # while has_more:
        #     result = client.delta(None)
        #     for path, metadata in result['entries']:
        #         # if path.startswith(settings.DROPBOX_DRAFTS_PATH):
        #             f.write("%s\n" % path)
        #             # f.write("%s\n" % metadata)
        #     has_more = result['has_more']

        # if (metadata is None or metadata['is_dir'] or not path.endswith('.md')):
        # f.write("%s\n" % client.metadata(settings.DROPBOX_DRAFTS_PATH))

