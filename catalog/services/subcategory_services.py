from catalog.models import Subcategory

def get_all_subcategories():
    return Subcategory.objects.all()

def get_subcategories_by_category(category_id):
    return Subcategory.objects.filter(category_id=category_id)
