from django.urls import path
from api import views

urlpatterns=[
    #user
    path('register/', views.register, name='register_user'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    #category
    path('category/', views.list_category),
    path('create-category/', views.create_category),
    #product
    path('product-all/', views.product_all),
    path('product-detail/<int:id>', views.product_detail),
    path('product-wish/', views.product_wish),
    path('product-review/', views.product_review),
    path('register/', views.register),
    #cart
    path('add-cart/', views.add_cart),
    path('cart/<int:id>', views.cart_detail),
    path('cart-delete/<int:id>', views.cart_delete),
    #order
    path('order/',views.order)
]