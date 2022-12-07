from django.shortcuts import render
from django.http import HttpResponse
from .readjson import read_json_file

# Create your views here.

def showjson_homepage(request):
    stock_market_data=  read_json_file('./stock_market_data.json')
    
    

 
    return render(request,'index.html',{'stock_market_data':stock_market_data})
