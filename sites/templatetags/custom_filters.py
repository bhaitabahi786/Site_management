# custom_filters.py
from django import template



register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.simple_tag
def custom_tag():
    # Your custom logic here
    return "Hello, World!"  # For example, return a fixed string

@register.filter
def TotalLabourCal():
    # Your custom logic here

    return "Hello, World!"


