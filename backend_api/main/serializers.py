from rest_framework import serializers
from . import models

#Vendors
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('id','name', 'user', 'address', 'phone', 'email')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1
        


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('id','name', 'user', 'address', 'phone', 'email')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs) 
        #self.Meta.depth = 1

#Products
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'category', 'title', 'description', 'price', 'vendor')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs) 
        #self.Meta.depth = 1

class ProductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = ('id', 'category', 'title', 'description', 'price', 'vendor', 'product_ratings')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs) 
        #self.Meta.depth = 1

#Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id','user', 'name', 'phone', 'address', 'email')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1
        


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id','user', 'name', 'phone', 'address', 'email')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs) 
        #self.Meta.depth = 1


#Orders
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'customer')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ('id', 'order', 'product')
        depth = 1

    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ('id', 'customer', 'address', 'default_address')
        depth = 1

    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ('id', 'customer', 'product', 'rating', 'reviews', 'add_time')
        depth = 1

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1

#Product Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ('id','title', 'description')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        #self.Meta.depth = 1
        


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ('id', 'title', 'description')
        depth = 1
    def __init__(self, *args, **kwargs):
        super(CategoryDetailSerializer, self).__init__(*args, **kwargs) 
        #self.Meta.depth = 1