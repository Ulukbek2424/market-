from catalog.models import Product
from .subcategory_services import *

def get_all_products():
    return Product.objects.all()

def get_products_by_subcategory(subcategory_id):
    return Product.objects.filter(subcategory_id=subcategory_id)

def get_products_by_category(category_id):
    subcategories = get_subcategories_by_category(category_id)
    return Product.objects.filter(subcategory__in=subcategories)

def get_product_by_id(product_id):
    return Product.objects.get(pk=product_id)
