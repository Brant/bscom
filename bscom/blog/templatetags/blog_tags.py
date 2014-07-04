"""

"""
from datetime import datetime

from django import template
from django.db.models import Q

from bscom.blog.models import Entry, Category


register = template.Library()


@register.filter
def get_related(entry, count=5):
    """
    Get related articles, randomly ordered, 5 of them
    """
    try:
        count = int(count)
    except ValueError:
        raise template.TemplateSyntaxError("The get_related template filter was passed '%s' as the 'count' argument, which needs to be an integer" % count)

    return Entry.objects.filter(
        ~Q(pk=entry.pk),
        external_link__isnull=True,
        date__lte=datetime.now(),
        draft=False,
        tags__name__in=[t for t in entry.tags.all()]
    ).distinct()[:5]


def blog_categories(context):
    """
    Renders a list of categories
    """
    categories = Category.objects.all()
    return {"categories": categories, "request": context["request"]}
register.inclusion_tag('blog/tags/category_list.html', takes_context=True)(blog_categories)


def blog_archives(context):
    """
    Renders list of archives, by month/year
    """
    entries = Entry.objects.filter(date__lte=datetime.now(), draft=False).dates('date', 'month', order='DESC')
    return {'archives': entries, 'request': context['request']}
register.inclusion_tag('blog/tags/archive_list.html', takes_context=True)(blog_archives)


def do_new_month(parser, token):
    try:
        tag_name, entry, true_false = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%s tag should be '%s ENTRY VAR_NAME'" % (token.contents.split()[0], token.contents.split()[0]))

    return NewMonth(entry, true_false)


class NewMonth(template.Node):
    def __init__(self, entry, true_false):
        self.entry = entry
        self.true_false = true_false

    def render(self, context):
        entry_month = context[self.entry].date.month

        if "BLOG_LAST_MONTH" not in context:
            context[self.true_false] = True
            context["BLOG_LAST_MONTH"] = entry_month
            return ""

        if entry_month != context["BLOG_LAST_MONTH"]:
            context[self.true_false] = True
            context["BLOG_LAST_MONTH"] = entry_month
        else:
            context[self.true_false] = False

        return ""

register.tag("new_month", do_new_month)
