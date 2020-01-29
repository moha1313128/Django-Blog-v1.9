try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3.X
from django import template

register = template.Library()

@register.filter
def urlify(value):
    return quote(value)