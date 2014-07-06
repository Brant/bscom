"""

"""
import dropbox

from django.core.management.base import BaseCommand
from django.conf import settings

from bscom.blog.tasks import import_drafts_from_dropbox

class Command(BaseCommand):

    def handle(self, *args, **options):
        import_drafts_from_dropbox()
