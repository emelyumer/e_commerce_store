from django.urls import path
from store.views import store, product_info, list_category


urlpatterns = [

    path('', store, name='store'),
    path('product/<slug:product_slug>/', product_info, name='product-info'),
    path('search/<slug:category_slug>/', list_category, name='list-category'),

]
