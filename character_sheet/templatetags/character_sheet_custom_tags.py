from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def format_modifier(modifier):
    if int(modifier) < 0:
        formatted_modifier = modifier
    else:
        formatted_modifier = f'+{modifier}'
    return formatted_modifier
