from django.urls import path
from .views import ProductAPI, CategoryAPI

urlpatterns = [
    path('category', CategoryAPI.as_view(), name='category'),
    path('category/<int:category_id>/', CategoryAPI.as_view(), name='category-detail'),
    path('', ProductAPI.as_view(), name='product'),
    path('<int:product_id>/', ProductAPI.as_view(), name='product-detail')
]