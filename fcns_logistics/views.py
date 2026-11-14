
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Route, Truck, Expense

@login_required
def dashboard_view(request):
    user = request.user
    
    # Si es conductor, solo ve sus rutas. Si es manager/admin, ve todas.
    if user.role == 'DRIVER':
        routes = Route.objects.filter(driver=user)
    else:
        routes = Route.objects.all()
        
    context = {
        'routes': routes,
        'user': user,
    }
    return render(request, 'fcns_logistics/dashboard.html', context)
