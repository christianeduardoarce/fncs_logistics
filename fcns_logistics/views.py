from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Route
from .forms import ExpenseForm
from django.shortcuts import get_object_or_404

@login_required
def route_detail_view(request, pk):
    route = get_object_or_404(Route, pk=pk)
    
    # Validar si es conductor y asegurarse de que solo vea sus propias rutas
    if request.user.role == 'DRIVER' and route.driver != request.user:
        return redirect('fcns_logistics:dashboard')
        
    expenses = route.expenses.all()
    total_expenses = sum(exp.amount for exp in expenses)
    
    context = {
        'route': route,
        'expenses': expenses,
        'total_expenses': total_expenses,
    }
    return render(request, 'fcns_logistics/route_detail.html', context)