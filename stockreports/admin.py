from django.contrib import admin
from .models import Stocks
# Register your models here.

class stockreportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticker', 'openPrice', 'closePrice', 'high', 'low')

admin.site.register(Stocks, stockreportsAdmin)