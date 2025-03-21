from django.urls import path
from .views import stock_chart

urlpatterns = [
    path('', stock_chart, name='stock_chart')
]
