"""
Blog admin configurations
"""
from django.contrib import admin
from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import get_current_site
from django.core.exceptions import ObjectDoesNotExist

from noodles.admin.actions import re_create_assets

from bscom.blog.models import Entry, Category


def reslug(modeladmin, request, queryset):
    """
    admin action to reset the slug of an entry

    creates a redirect too

    - If the slug hasnt changed, do nothing
    - If the redirect already exists, don't create a new redirect
    - If there is a redirect that will send this into a loop,
        remove that redirect and create a new one
    """
    for obj in queryset:
        old_url = obj.get_absolute_url()

        obj.slug = None
        obj.save()

        if old_url != obj.get_absolute_url():
            try:
                redirect = Redirect.objects.get(site=get_current_site(request), old_path=old_url, new_path=obj.get_absolute_url())
            except ObjectDoesNotExist:
                try:
                    looping_redirect = Redirect.objects.get(site=get_current_site(request), old_path=obj.get_absolute_url(), new_path=old_url)
                    looping_redirect.delete()
                except ObjectDoesNotExist:
                    pass
                redirect = Redirect(site=get_current_site(request), old_path=old_url, new_path=obj.get_absolute_url())
                redirect.save()

reslug.short_description = "Re-slug"


class EntryAdmin(admin.ModelAdmin):
    """
    Blog Entry admin configuration
    """
    actions = [reslug, re_create_assets]

    fieldsets = (
        (None, {
            "fields": ["title", "slug", "content", "blurb", "thumbnail", ]
        }),
        ("For Links", {
            "fields": ["external_link"]
        }),
        ("Draft Info", {
            "fields": ["draft", "draft_file",  'date_modified']
        }),
        ("Metadata", {
            "fields": ["date", "category", "tags", ]
        })
    )

    list_display = ["title", "slug", "date", "category"]
    list_filter = ["category", "draft", ]
    readonly_fields = ['draft_file', 'date_modified', 'slug', ]


admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)
