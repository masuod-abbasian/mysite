from django.shortcuts import render
from django.http import HttpResponse

def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def maintenance(request):
    return render(request, 'errors/maintenance.html')

