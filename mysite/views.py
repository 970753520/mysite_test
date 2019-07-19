from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    #return HttpResponse('hello word')
    context={}
    return render_to_response('home.html',context)
