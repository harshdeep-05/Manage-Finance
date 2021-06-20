from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses'),
    path('add_expense',views.add_expense, name='add_expense'),
    path('expense_category_summary',views.expense_category_summary, name="expense_category_summary"),
    path('stats',views.stats, name='stats'),
]
