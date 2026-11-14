from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Route
from .forms import ExpenseForm

@login_required
def dashboard_view(request):
    user = request.user
    if user.role == 'DRIVER':
        routes = Route.objects.filter(driver=user)
    else:
        routes = Route.objects.all()
        
    context = {
        'routes': routes,
        'user': user,
    }
    return render(request, 'fcns_logistics/dashboard.html', context)

@login_required
def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('fcns_logistics:dashboard')
    else:
        form = ExpenseForm(user=request.user)
        
    return render(request, 'fcns_logistics/add_expense.html', {'form': form})

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