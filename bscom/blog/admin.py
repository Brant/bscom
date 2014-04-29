"""
Blog admin configurations
"""
from django.contrib import admin

from bscom.blog.models import Entry, Category


def reslug(modeladmin, request, queryset):
    for obj in queryset:
        obj.slug = None
        obj.save()
reslug.short_description = "Re-slug"


class EntryAdmin(admin.ModelAdmin):
    """
    Blog Entry admin configuration
    """
    actions = [reslug, ]
    fieldsets = (
        (None, {
            "fields": ["title", "slug", "content", "blurb", "thumbnail", ]
        }),
        ("For Links", {
            "fields": ["external_link"]
        }),
        ("Metadata", {
            "fields": ["category", "tags", ]
        })
    )

    list_display = ["title", "slug", "date", "category"]
    list_filter = ["category"]
    readonly_fields = ["slug", ]

admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)
