from django.db import models

# Create your models here.

class Stocks(models.Model):
    name = models.CharField(max_length=120)
    ticker = models.CharField(max_length=120)
    openPrice = models.FloatField()
    closePrice = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()

    def _str_(self):
        return self.name
    
    def should_buy(self):
        return True
