from django.shortcuts import render
from catalog.services.category_services import *
from catalog.services.product_services import *
from catalog.services.subcategory_services import *


def catalog(request):
    products = get_all_products()
    context = {
        'products': products,
    }
    return render(request, 'catalog/catalog.html', context=context)


def catalog_by_category(request, category_id):
    category = get_category_by_id(category_id)
    products = get_products_by_category(category_id)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'catalog/catalog_by_category.html', context=context)


def catalog_by_subcategory(request, category_id, subcategory_id):
    category = get_category_by_id(category_id)
    products = get_products_by_subcategory(subcategory_id)
    context = {
        'category' : category,
        'products': products,
    }
    return render(request, 'catalog/catalog_by_subcategory.html', context=context)


def product_page(request, product_id):
    product = get_product_by_id(product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_page.html', context=context)
