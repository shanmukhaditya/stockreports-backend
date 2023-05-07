from django.contrib import admin
from .models import Stocks
# Register your models here.

class stockreportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'dashboardId', 'dashboardName', 'ticker')

admin.site.register(Stocks, stockreportsAdmin)