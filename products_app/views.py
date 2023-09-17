from django.shortcuts import render
from products_app.serializers import ProductSerializer
from products_app.models import Product
from rest_framework import  viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer