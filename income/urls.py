from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='income'),
    path('add_income',views.add_income, name='add_income'),
    path('income_category_summary',views.income_category_summary, name="income_category_summary"),
    path('income_stats',views.income_stats, name='income_stats'),
]
