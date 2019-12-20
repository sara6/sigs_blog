from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    url = "http://api.planetos.com/v1/datasets"

    querystring = {"apikey":"XXX"}

    response = requests.request("GET", url, params=querystring)

    result = response.json()

    return render(request, 'home.html', { 'result': result})
