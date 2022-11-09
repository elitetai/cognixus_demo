import re 
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='show_code_only')
def show_code_only(value, search):
    text = re.compile(search).search(value).group()
    return mark_safe(text)