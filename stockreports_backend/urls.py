"""
URL configuration for stockreports_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from stockreports import views

router = routers.DefaultRouter()
router.register(r'stockreports', views.StockView, 'stockreports')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/addStock/', views.add_stock, name='add-stock'),
    path('api/dashboard/<int:id>/', views.get_stock_by_id, name='get-dashboard'),
    path('api/getAll/', views.getAll, name='get-all-stocks'),
    path('api/getStocksByDashboardId/<int:id>/', views.get_stocks_by_dashboard_id, name='get-stocks-by-dashboard-id'),
    path('api/getCompanies/', views.get_companies, name='get-companies'),
    path('api/getGraphByTicker/<str:ticker>/', views.get_graph_by_ticker, name='get-graph-by-ticker')
]
