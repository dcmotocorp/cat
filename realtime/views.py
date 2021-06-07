from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime 
import time 
# Create your views here.

def index(request):
    now =datetime.now()
    time_formate=now.strftime("%H:%M:%S")
    print(time_formate)
    return render(request,"realtime/index.html",{'time':time_formate})

def gettime(request):
    now =datetime.now()
    time_formate=now.strftime("%H:%M:%S")
    return JsonResponse({'time':time_formate})
