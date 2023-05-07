from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import StockSerializer
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import yfinance as yf
# Create your views here.

class StockView(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stocks.objects.all()

@api_view(['POST'])
def add_stock(request):
    data = request.data
    data['name'] = companies[data['ticker']]
    serializer = StockSerializer(data=data)
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
    return Response([serializer.data])

@api_view(['GET'])
def getAll(request):
    stocks = Stocks.objects.all().order_by('dashboardId', 'dashboardName')
    data = []
    for stock in stocks:
        if not data or data[-1]['id'] != stock.dashboardId:
            data.append({'id': stock.dashboardId, 'name': stock.dashboardName, 'stocks': []})
        serializer = StockSerializer(stock)
        print(serializer.data)
        data[-1]['stocks'].append({'id': serializer.data['id'] + number, 
                                   'name': serializer.data['name'], 
                                   'suggest': serializer.data['suggest'],
                                   'ticker': serializer.data['ticker'],
                                   'openPrice': serializer.data['openPrice'],
                                   'closePrice':serializer.data['closePrice']
                                   })
    return Response(data)

@api_view(['GET'])
def get_stocks_by_dashboard_id(request, id):
    try:
        stock = Stocks.objects.filter(dashboardId=id)
    except Stocks.DoesNotExist:
        return Response(status=404)

    serializer = StockSerializer(stock, many=True)
    return Response([serializer.data])

@api_view(['GET'])
def get_companies(request):
    data = []
    for k, v in companies.items():
        data.append({'ticker': k, 'company' : v})
    return Response(data)

@api_view(['GET'])
def get_graph_by_ticker(request, ticker):
    ticker = yf.Ticker(ticker)
    df = ticker.history(period='12mo')
    data = []
    for index, row in df.iterrows():
        data.append({'name':index.strftime('%m/%d'), 'price': row['Close']})
    return Response(data)