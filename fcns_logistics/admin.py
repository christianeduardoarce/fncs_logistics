from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Truck, Route

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_staff', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol Personalizado', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Truck)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
 list_display = ['origin', 'destination', 'truck', 'driver', 'status', 'departure_date']
list_filter = ['status', 'departure_date']
search_fields = ['origin', 'destination', 'truck__license_plate', 'driver__username']

