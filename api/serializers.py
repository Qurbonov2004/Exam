from rest_framework import serializers
from main import models




class UserSer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields='__all__'




class CategorySer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields=['title']





class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields='__all__'




class ProductImageSer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductImage
        fields='__all__'





class ReviewSer(serializers.ModelSerializer):
    class Meta:
        model=models.Review
        fields='__all__'



class WishlistSer(serializers.ModelSerializer):
    class Meta:
        model=models.Wishlist
        fields='__all__'





class CartSer(serializers.ModelSerializer):
    class Meta:
        model=models.Cart
        fields='__all__'




class OrderSer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields='__all__'


