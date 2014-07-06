from __future__ import absolute_import

from dateutil import parser

import dropbox

from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

from bscom.blog.models import Entry

# from baseline.queue.celery import app


@shared_task
def import_drafts_from_dropbox():
    """
    Imports .md files from a specified settings.DROPBOX_DRAFTS_PATH
    """
    client = dropbox.client.DropboxClient(settings.DROPBOX_TOKEN)

    for item in client.metadata(settings.DROPBOX_DRAFTS_PATH)['contents']:
        if item['path'].endswith(".md"):
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
