from django import template

register = template.Library()


@register.filter
def get_dict_value(value, arg):
    return value[arg]
