from django.contrib import admin

from bscom.blog.models import Entry, Category

class EntryAdmin(admin.ModelAdmin):
    """
    Blog Entry admin configuration
    """
    list_display = ["title", "date", "category"]
    list_filter = ["category"]
    
admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)