from django import template
register = template.Library()

@register.filter(is_safe=True)
def nongban_auth(value,prefix):
    return prefix+value