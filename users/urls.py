from django.urls import path
from .views import (create_user, login_user, logout_user, create_product, list_products, product_detail, update_product,
                    delete_product)

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('products/', list_products, name='list_products'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/update/', update_product, name='update_product'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product'),

]
