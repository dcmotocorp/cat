
from django.shortcuts import render
from .models import * 
# Create your views here.
def index(request):

    m1=Group.objects.filter(id=1)
    m1.entry_set.clear()
    return render(request,"relation/index.html")