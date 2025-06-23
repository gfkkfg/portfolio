from django import template

register = template.Library()

@register.filter
def split_by(value, delimiter=','):
    return [item.strip() for item in value.split(delimiter)]
