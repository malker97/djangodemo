from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    ipaddr = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
    return HttpResponse("Test GCP Cloud Run CD Trigger status from IP: " + ipaddr)
