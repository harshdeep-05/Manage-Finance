from django.shortcuts import render,redirect
from .models import Income, Source
from django.core.paginator import Paginator
import datetime
import json
from django.http import JsonResponse
# Create your views here.

def index(request):
    sources = Source.objects.all()
    income=Income.objects.all()
    
    #paginator = Paginator(incomes, 5)      
    #page_number = request.GET.get('page')
    #page_obj = Paginator.get_page(paginator, page_number)
    
    context={
        'income':income,
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
        amount = request.POST['amount']
        date = request.POST['date']
        source = request.POST['source ']
        description = request.POST['description']
          
        Income.objects.create(amount=amount, source=source, description=description,date=date)
        return redirect('income')
    
def income_category_summary(request):
    today_date=datetime.date.today()
    six_months_ago=today_date-datetime.timedelta(days=30*6)
    income=Income.objects.filter(owner=request.user, 
        date__gte=six_months_ago,date__lte=today_date)
    finalrep = {}

    def get_category(income):
        return income.category

    category_list= list(set(map(get_category,income)))

    def get_income_category_amount(category):
        amount=0
        filtered_by_category=income.filter(category=category)

        for item in filtered_by_category:
            amount+=item.amount

        return amount

    for x in income:
        for y in category_list:
            finalrep[y]=get_income_category_amount(y)    

    return JsonResponse({'income_category_data':finalrep},safe=False)

def income_stats(request):
    return render(request, 'income/stats.html')