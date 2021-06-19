from abc import ABCMeta
from django.shortcuts import render,redirect
from .models import Income, Source
from django.core.paginator import Paginator
import datetime
# Create your views here.

def index(request):
    sources = Source.objects.all()
    incomes=Income.objects.all()
    
    #paginator = Paginator(incomes, 5)      
    #page_number = request.GET.get('page')
    #page_obj = Paginator.get_page(paginator, page_number)
    
    context={
        'income':incomes,
        #'page_obj': page_obj,
    }
    return render(request,'income/index.html',context)

def add_income(request):
    sources = Source.objects.all()
    
    context ={
        'sources' : sources,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'income/add_income.html', context)    
    
    if request.method == 'POST':
        Income.objects.create(amount=amount, date=date, source=source, description=description)
        return redirect('income')
    
