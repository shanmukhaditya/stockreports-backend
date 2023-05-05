from rest_framework import serializers
from .models import Stocks

class StockSerializer(serializers.ModelSerializer):
    should_buy = serializers.SerializerMethodField()

    class Meta:
        model = Stocks
        fields = '__all__'
    
    def get_should_buy(self, obj):
        return obj.should_buy()