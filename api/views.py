#Proyect
from main import models

#Django
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

#Rest framework
from api import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token




#User
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = serializers.UserSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token= Token.objects.create(user=user)
            return Response({"message": "User logged in successfully.",
                             "token":token}, status=200)
        else:
            return Response({"error": "Invalid username or password."}, status=401)
        




# Foydalanuvchi tizimdan chiqish
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'PUT':
        logout(request)
        return Response({"message": "User logged out successfully."}, status=200)
    




# Profilni tahrirlash
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    if request.method == 'PUT':
        user = request.user
        username = request.data.get('username')
        email = request.data.get('email')
        user.username = username
        user.email = email
        user.save()
        return Response({"message": "Profile updated successfully."}, status=200)
    




# Profilni o'chirish
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return Response({"message": "Profile deleted successfully."}, status=204)




#category
@api_view(['GET'])
def list_category(request):
    categories = models.Category.objects.all()
    category_ser = serializers.CategorySer(categories, many=True)
    return Response(category_ser.data)




@api_view(['POST'])
def create_category(request):
    data=request.data
    serializer=serializers.CategorySer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




#Product
@api_view(['GET'])
def product_all(request):
    products=models.Product.objects.all()
    products_ser=serializers.ProductSer(products,many=True)
    return Response(products_ser.data)



@api_view(['GET'])
def product_detail(request,id):
    product_image=models.ProductImage.objects.filter(product_id=id)
    product_image_ser=serializers.ProductImageSer(product_image,many=True)
    product=models.Product.objects.get(id=id)
    product_ser=serializers.ProductSer(product)
    product_ser.data['images']=product_image_ser.data
    return Response(product_ser.data)



#Product wishlist
@api_view(['POST'])
def product_wish(request):

    serializer=serializers.WishlistSer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




#product review
@api_view(['POST'])
def product_review(request):
    serializer=serializers.ReviewSer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




    
#Cart



@api_view(['POST'])
def add_cart(request):
    product_id = request.data.get('product_id')
    print(request.user)
    if product_id is None:
        return Response({"error": "Product ID is required."}, status=400)
    product = get_object_or_404(models.Product, id=product_id)
    user = request.user
    active_cart = models.Cart.objects.filter(customer=user, is_active=True).first()
    if not active_cart:
        active_cart = models.Cart.objects.create(customer=user)

    existing_product = models.CartProduct.objects.filter(cart=active_cart, product=product).first()

    if existing_product:
        existing_product.quantity += 1
        existing_product.save()
    else:
        models.CartProduct.objects.create(cart=active_cart, product=product, quantity=1)

    return Response({"message": "Product added to cart successfully."}, status=201)

@api_view(['GET'])
def cart_detail(request, id):
    try:
        cart = models.Cart.objects.get(id=id)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = models.CartSerializer(cart)
        return Response(serializer.data)
    

@api_view(['DELETE'])
def cart_delete(request,id):
    cart = models.Cart.objects.get(id=id)
    cart.delete()
    Response(status=status.HTTP_200_OK)




@api_view(['POST'])
def order(request):
    cart=models.Cart.objects.get(user=request.user,is_active=True)
    for cart_product in cart.cartproduct_set.all():
        cart_product.product.quantity -= cart_product.quantity
        cart_product.product.save()
    models.Order.objects.create(
        cart=cart,
        customer=request.user
    )

    cart.is_active=False
    cart.save()
    return Response(status=status.HTTP_202_ACCEPTED)
