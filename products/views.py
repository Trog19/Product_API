from itertools import product
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