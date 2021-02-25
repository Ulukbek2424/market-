from django.urls import path

from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('category/<int:category_id>/', catalog_by_category, name='category'),
    path('category/<int:category_id>/<int:subcategory_id>/',catalog_by_subcategory, name='subcategory'),
    path('product/<int:product_id>/', product_page, name='product'),
]
