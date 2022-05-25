from itertools import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer



@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()

    serializers = ProductSerializer(products, many=True)

    return Response(serializers.data)