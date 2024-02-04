
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from menus.models import Menu

# Create your views here.
def index(request):
    context = dict()
    today = datetime.now().date()
    menus = Menu.objects.all()
    context["today"] = today
    context["menus"] = menus
    return render(request, 'menus/index.html',context=context)

def detail(request,pk):
    context= dict()
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    return render(request,'menus/detail.html',context=context)