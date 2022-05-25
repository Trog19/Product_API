from itertools import product
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from rest_framework import status

from products import serializers



@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)


    elif request.method =='POST':
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        serializers= ProductSerializer(product)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = ProductSerializer(product, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)