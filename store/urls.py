from django.urls import path
from .views import *

urlpatterns = [
    path('', store_view, name='store-page'),
    path('<str:category_slug>/', store_view, name='cat-products-page'),
    path('<str:category_slug>/<str:product_slug>/', product_detail_view, name='prod-detail-page'),
]

