from rest_framework import serializers
from .models import Stocks

class StockSerializer(serializers.ModelSerializer):
    openPrice = serializers.SerializerMethodField()
    closePrice = serializers.SerializerMethodField()
    suggest = serializers.SerializerMethodField()

    class Meta:
        model = Stocks
        fields = '__all__'
    
    def get_suggest(self, obj):
        return False if obj.get_openPrice() - obj.get_closePrice() > 0 else True
    
    def get_openPrice(self, obj):
        return str(obj.get_openPrice())

    def get_closePrice(self, obj):
        return str(obj.get_closePrice())