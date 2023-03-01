from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    # use ipinfo.io to get the IP address of the server
    ipinfo = requests.get('https://ipinfo.io')
    ipinfo_json = ipinfo.json()
    ip = ipinfo_json['ip']
    ipaddr = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
    return HttpResponse(ipaddr + "<-" + ip)
