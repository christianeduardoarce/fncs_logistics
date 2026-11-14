from django.urls import path
from .views import (
    dashboard_view, 
    add_expense_view, 
    route_detail_view, 
    CustomLoginView, 
    CustomLogoutView
)

app_name = 'fcns_logistics'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('gastos/nuevo/', add_expense_view, name='add_expense'),
    path('ruta/<uuid:pk>/', route_detail_view, name='route_detail'),
]