from django.shortcuts import render,redirect
from .models import Category, Expense
from django.core.paginator import Paginator
import datetime
# Create your views here.

def index(request):
    categories = Category.objects.all()
    expenses=Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)      
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context={
        'expenses':expenses,
        'page_obj': page_obj,
    }
    return render(request,'expenses/index.html')

def add_expense(request):
    categories = Category.objects.all()
    context ={
        'categories' : categories,
        'values': request.POST
    }
    return render(request, 'expenses/add_expense.html',context)
    
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)    
    
    if request.method == 'POST':
        amount = request.POST['amount']
    