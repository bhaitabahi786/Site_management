# custom_filters.py
from django import template

register = template.Library()

@register.filter
def getkey(dict, key, default=None):
    return dict.get(key, default)


