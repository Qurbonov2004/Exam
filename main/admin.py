from django.contrib import admin
from main import models

admin.site.register(models.User)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.Review)
admin.site.register(models.Wishlist)
admin.site.register(models.Category)
admin.site.register(models.Order)
admin.site.register(models.Cart)
admin.site.register(models.CartProduct)
