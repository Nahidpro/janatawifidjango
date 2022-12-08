from django.shortcuts import render
from django.http import HttpResponse 
from .models import jatatawifi_stock_market
from datetime import datetime

# Create your views here.
def show_sqlmodel(request):
    stock_market_data = list(jatatawifi_stock_market.objects.order_by('-date')[:20])
    if request.method == 'POST':
        datee = request.POST['date']
        trade_code = request.POST['trade_code']
        high = request.POST['high']
        low = request.POST['low']
        date = datetime.strptime(datee,'%Y-%m-%d')
        open = request.POST['open']
        close = request.POST['close']
        update_stock_data = jatatawifi_stock_market(date=date, trade_code=trade_code, high=high, low=low,open=open, close=close)
        update_stock_data.save()
    
    
    trdecode_market_data = list(jatatawifi_stock_market.objects.order_by('-date') [:50])
    trade_code_name = [] 
    for obj in trdecode_market_data:
        if obj.trade_code not in trade_code_name:
            trade_code_name.append(obj.trade_code)
    
    
    
    return render(request,'janatawifi.html',{'stock_market_data':stock_market_data, "trade_code_name":trade_code_name })


