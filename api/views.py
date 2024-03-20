from main import models
from api import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from django.contrib.auth import login,logout,authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = serializer.UserSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['GET'])
def list_category(request):
    """ Barcha category lar"""
    categories = models.Category.objects.all()
    category_ser = serializers.CategorySer(categories, many=True)
    print(category_ser.data)
    return Response(category_ser.data)


@api_view(['POST'])

def create_category(request):
    """ Category yaratish """
    data=request.data
    serializer=serializers.CategorySer(data=data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_all(request):
    """ Barcha Maxsulotlar """
    products=models.Product.objects.all()
    print(products)
    products_ser=serializers.ProductSer(products,many=True)
    print(products_ser.data)
    return Response(products_ser.data)



@api_view(['GET'])
def product_detail(request,id):
    """ Maxsulot ma'lumotlari """
    product=models.Product.objects.get(id=id)
    product_ser=serializers.ProductSer(product)
    return Response(product_ser.data)



@api_view(['POST'])
def product_wish(request):
    """ Yoqtirganlarga qo'shish va olib tashlash """
    serializer=serializers.WishlistSer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def product_review(request):
    """ Baho berish va uni tahrirlash"""
    serializer=serializers.ReviewSer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




    








# USER
# Register -> POST
# Log in -> POST
# Log out -> PUT
# Edit Profile -> PUT
# Delete Profile -> DELETE

# ALL products -> GET
# Product detail -> GET
# Add Product to wishlsit -> POST
# Remove Product from wishlist -> POST ///
# Give Review -> POST
# Add Product to Cart -> POST
# Remove Product from Cart - POST
# Order Cart - POST
# Cancel Order - POST