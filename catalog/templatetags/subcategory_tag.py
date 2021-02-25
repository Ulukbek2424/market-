from django import template
from catalog.services.subcategory_services import *

register = template.Library()

@register.simple_tag()
def subcategories_by_category(category_id):
    subcategories = get_subcategories_by_category(category_id)
    return subcategories
