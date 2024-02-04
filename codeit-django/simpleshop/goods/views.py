from django.shortcuts import render
from goods.models import Product

# Create your views here.
def index(request):
    context={}
    goods = Product.objects.all()
    context["goods"]=goods
    return render(request,'goods/index.html',context=context)