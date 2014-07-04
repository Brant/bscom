"""

"""
import dropbox

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        # flow = dropbox.client.DropboxOAuth2FlowNoRedirect(settings.DROPBOX_APP_KEY, settings.DROPBOX_SECRET)
        # authorize_url = flow.start()
        # print '1. Go to: ' + authorize_url
        # print '2. Click "Allow" (you might have to log in first)'
        # print '3. Copy the authorization code.'
        # code = raw_input("Enter the authorization code here: ").strip()
        # access_token, user_id = flow.finish(code)
        client = dropbox.client.DropboxClient(settings.DROPBOX_TOKEN)
        print client.metadata(settings.DROPBOX_DRAFTS_PATH)['contents']
