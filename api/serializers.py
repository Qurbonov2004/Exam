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






class ProductImageSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'

class ProductSer(serializers.ModelSerializer):
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = '__all__'

    def get_product_image(self, obj):
        images = models.ProductImage.objects.filter(product=obj)
        serializer = ProductImageSer(images, many=True)
        return serializer.data


class ReviewSer(serializers.ModelSerializer):
    class Meta:
        model=models.Review
        fields='__all__'



class WishlistSer(serializers.ModelSerializer):
    class Meta:
        model=models.Wishlist
        fields='__all__'


class OrderSer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields='__all__'



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Cart
        fields = ['id', 'is_active', 'customer', 'cart_items']