from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(name='highlight_tags')
def highlight_tags(text):
    if not isinstance(text, str):
        return text


    # emails
    text = re.sub(
        r'([\w\.-]+@[\w\.-]+\.\w+)',
        r'<a href="mailto:\1">\1</a>',
        text
    )

    # URLs with http/https
    text = re.sub(
        r'(https?://[^\s]+)',
        r'<a href="\1" target="_blank">\1</a>',
        text
    )

    # URLs with www. 
    text = re.sub(
        r'\b(www\.[^\s]+)',
        r'<a href="http://\1" target="_blank">\1</a>',
        text
    )

    # @
    text = re.sub(
        r'(?<![\w@])(@\w+)',
        r'<span class="text-primary">\1</span>',
        text
    )

    # Hashtags
    text = re.sub(
        r'(?<!\w)(#\w+)',
        r'<span class="text-success">\1</span>',
        text
    )

    return mark_safe(text)