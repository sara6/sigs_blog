from django.shortcuts import render

def maps(request):
    mapbox_access_token = ''
    return render(request, 'maps.html',
                  { 'mapbox_access_token': mapbox_access_token })
