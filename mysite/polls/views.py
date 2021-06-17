from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import *

# Create your views here.

def login_view(request):
    return render(request,'login.html')

def loginsuc(request):
    u = request.POST.get("judge1",'')
    v = request.POST.get("judge2",'')

    if u and v:
        c=UserInfo.objects.filter(id=u,info=v).count()
        if c>=1:
            return HttpResponse("successful")
        else:
            return HttpResponse("fail")

# 记得保存用户数据
def trial(request):
    if(request.method =='GET'):
        u=UserInfo.objects.all()
        json_data = serialize('json',u)
        return HttpResponse(json_data,content_type="application/json")
        #return HttpResponse(json_data)





