from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Fileinfo

# Create your views here.

def file_info(request,fileinfo_id):
    fileinfos = Fileinfo.objects.get(id=fileinfo_id)
    return Hrender_to_response('文章：%s',context)


def fileinfo_all(request):
    fileinfos = Fileinfo.objects.all()
    context = {}
    context['fileinfos'] = fileinfos
    return render_to_response('fileinfo.html',context)
