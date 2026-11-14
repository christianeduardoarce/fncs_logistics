from django import forms
from .models import Expense, Route

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['route', 'category', 'amount', 'description']
        labels = {
            'route': 'Ruta',
            'category': 'Categoría de Gasto',
            'amount': 'Monto ($)',
            'description': 'Descripción o Notas',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.role == 'DRIVER':
            self.fields['route'].queryset = Route.objects.filter(driver=user)