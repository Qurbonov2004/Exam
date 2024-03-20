from django.urls import path
from api import views

urlpatterns=[
    # path('user/<int:id>', views.user_detail),
    # path('create-user/', views.create_user),
    # path('delete-user/', views.delete_user),
    path('category/', views.list_category),
    path('create-category/', views.create_category),
    path('product-all/', views.product_all),
    path('product-detail/<int:id>', views.product_detail),
    path('product-wish/', views.product_wish),
    path('product-review/', views.product_review),
    path('register/', views.register),

]