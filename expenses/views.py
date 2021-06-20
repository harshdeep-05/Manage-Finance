from django.shortcuts import render,redirect
from .models import Category, Expense
from django.core.paginator import Paginator
import datetime
import json
from django.http import JsonResponse
# Create your views here.

def index(request):
    categories = Category.objects.all()
    expenses=Expense.objects.filter(owner=request.user)

    #paginator = Paginator(expenses, 5)      
    #page_number = request.GET.get('page')
    #page_obj = Paginator.get_page(paginator, page_number)
    
    context={
        'expenses':expenses,
        #'page_obj': page_obj,
    }
    return render(request,'expenses/index.html',context)

def add_expense(request):
    categories = Category.objects.all()
    context ={
        'categories' : categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)    
    
    if request.method == 'POST':
        amount = request.POST['amount']
        date = request.POST['date']
        category = request.POST['category']
        description = request.POST['description']
        Expense.objects.create(amount=amount ,date=date , category=category, description=description)  
        return redirect('expense')

def expense_category_summary(request):
    today_date=datetime.date.today()
    six_months_ago=today_date-datetime.timedelta(days=30*6)
    expenses=Expense.objects.filter(owner=request.user, 
        date__gte=six_months_ago,date__lte=today_date)
    finalrep = {}

    def get_category(expense):
        return expense.category

    category_list= list(set(map(get_category,expenses)))

    def get_expense_category_amount(category):
        amount=0
        filtered_by_category=expenses.filter(category=category)

        for item in filtered_by_category:
            amount+=item.amount

        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y]=get_expense_category_amount(y)    

    return JsonResponse({'expense_category_data':finalrep},safe=False)

def stats(request):
    return render(request, 'expenses/stats.html')    