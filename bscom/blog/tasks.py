from __future__ import absolute_import

from datetime import datetime
from dateutil import parser

import hmac
import hashlib
import base64
import dropbox

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import utc

from celery import shared_task

from bscom.blog.models import Entry

# from baseline.queue.celery import app


@shared_task
def import_drafts_from_dropbox():

    client = dropbox.client.DropboxClient(settings.DROPBOX_TOKEN)

    for item in client.metadata(settings.DROPBOX_DRAFTS_PATH)['contents']:
        mod_time = parser.parse(item['modified'])

        try:
            entry = Entry.objects.get(draft_file=item['path'])
        except ObjectDoesNotExist:
            entry = Entry(draft_file=item['path'], draft=True)

        if entry.draft and (not entry.date_modified or entry.date_modified < mod_time):
            f, metadata = client.get_file_and_metadata(item['path'])
            lines = f.readlines()
            title = lines[0].strip().replace("#", "")
            body = "".join(lines[1:])
            entry.content = body.strip()
            entry.title = title
            entry.save()



        # f, metadata = client.get_file_and_metadata(item['path'])
        # lines = f.readlines()
        # print lines

    # with open("/home/brant/bscom16/task.log", "a") as f:
    #     f.write("Updated... %s\n" % datetime.utcnow().replace(tzinfo=utc))
    #     f.write("%s\n" % client.metadata(settings.DROPBOX_DRAFTS_PATH))


        # f.write("Updated... %s\n" % datetime.now())
        # f.write("%s\n" % request.body)

        # f.write("%s\n" % request.META['HTTP_X_DROPBOX_SIGNATURE'])
        # f.write("%s\n" % signature)

        #
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

