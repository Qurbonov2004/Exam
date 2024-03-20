from django.db import models
from django.contrib.auth.models import AbstractUser,User
from functools import reduce




class Category(models.Model):
    title=models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title





class Product(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    baner_image=models.ImageField(upload_to='baner_image/')
    description=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()

    @property
    def review(self):
        reviews = Review.objects.filter(product_id=self.id)
        result = reduce(lambda result, x: result +x.mark, reviews, 0)
        try: 
            result = round(result / reviews.count())

        except  ZeroDivisionError:
            result=0
        return result
    
    def __str__(self):
        return self.name
    





class ProductImage(models.Model):
    image=models.ImageField(upload_to='product/_images')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)




class Review(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    mark=models.SmallIntegerField()


    def save(self, *args, **kwargs):
        object = Review.objects.filter(user=self.user, 
        product=self.product)
        if object.count():
            object.delete()
            super(Review, self).save(*args, **kwargs)
        else:
            super(Review, self).save(*args, **kwargs)




class Wishlist(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        try:
            object=Wishlist.objects.get(product=self.product, user=self.user)
            object.delete()
        except Wishlist.DoesNotExist:
            super().save(*args, **kwargs)

            


class Cart(models.Model):
    is_active=models.BooleanField(default=True)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ManyToManyField('CartProduct', related_name='cart_items')

    @property
    def quantity(self):
        return self.products.count()

    @property
    def total_price(self):
        total_price = sum(product.price for product in self.products.all())
        return total_price



class CartProduct(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)




class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_data=models.DateTimeField(auto_now_add=True)
