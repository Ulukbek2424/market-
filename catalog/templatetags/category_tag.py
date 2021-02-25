from django import template
from catalog.services.category_services import *

register = template.Library()

@register.simple_tag()
def all_categories():
    categories = get_all_categories()
    return categories
