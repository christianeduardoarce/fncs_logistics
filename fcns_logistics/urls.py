from django.urls import path
from .views import dashboard_view, add_expense_view

app_name = 'fcns_logistics'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('gastos/nuevo/', add_expense_view, name='add_expense'),
]
