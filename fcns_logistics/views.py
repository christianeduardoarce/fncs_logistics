from django.shortcuts import render, redirect
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