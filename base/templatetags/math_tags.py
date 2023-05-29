from django import template

register = template.Library()

@register.simple_tag
def multiply_values(value1, value2):
    return value1 * value2

@register.simple_tag
def devide_values(value1, value2):
    return value1 / value2
