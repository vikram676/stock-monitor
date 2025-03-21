from django.shortcuts import render
from .models import StockData

def stock_chart(request):
    data = StockData.objects.order_by('-timestamp')[:20]
    
    context = {
        'labels': [d.timestamp.strftime('%H:%M') for d in data],
        'open_prices': [d.open_price for d in data],
        'close_prices': [d.close_price for d in data],
    }
    return render(request, 'chart.html', context)

