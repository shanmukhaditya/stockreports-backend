from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import StockSerializer
from .models import Stocks
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class StockView(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stocks.objects.all()

@api_view(['POST'])
def add_stock(request):
    serializer = StockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_stock_by_id(request, id):
    try:
        stock = Stocks.objects.get(id=id)
    except Stocks.DoesNotExist:
        return Response(status=404)

    serializer = StockSerializer(stock)
    return Response(serializer.data)