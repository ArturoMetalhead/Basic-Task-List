from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(name='highlight_tags')
def highlight_tags(text):
    if not isinstance(text, str):
        return text


    # Correos primero (para que no se partan por el @)
    text = re.sub(
        r'([\w\.-]+@[\w\.-]+\.\w+)',
        r'<a href="mailto:\1">\1</a>',
        text
    )

    # URLs con http/https
    text = re.sub(
        r'(https?://[^\s]+)',
        r'<a href="\1" target="_blank">\1</a>',
        text
    )

    # URLs que empiezan con www. (y no están ya con http)
    text = re.sub(
        r'\b(www\.[^\s]+)',
        r'<a href="http://\1" target="_blank">\1</a>',
        text
    )

    # Menciones (@usuario), pero solo si no forman parte de un mail
    text = re.sub(
        r'(?<![\w@])(@\w+)',
        r'<span class="text-primary">\1</span>',
        text
    )

    # Hashtags (#tema)
    text = re.sub(
        r'(?<!\w)(#\w+)',
        r'<span class="text-success">\1</span>',
        text
    )

    return mark_safe(text)


    # text = re.sub(r'([\w\.-]+@[\w\.-]+\.\w+)', r'<a href="mailto:\1">\1</a>', text)
    # text = re.sub(r'(https?://[^\s]+)', r'<a href="\1">\1</a>', text)
    # text = re.sub(r'(@\w+)', r'<span class="text-primary">\1</span>', text)
    # text = re.sub(r'(#\w+)', r'<span class="text-success">\1</span>', text)
    
    # return mark_safe(text)