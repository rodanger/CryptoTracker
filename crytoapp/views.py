import requests
from django.shortcuts import render
from django.conf import settings
import json

# Create your views here.

def index(request):
    # Fetching Data
    apidata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    # We've our data in apidata variable
    return render(request,'index.html', {'apidata':apidata})

   