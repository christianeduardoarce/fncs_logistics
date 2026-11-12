import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('DRIVER', 'Conductor'),
        ('MANAGER', 'Gestor'),
        ('ADMIN', 'Administrador'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='DRIVER')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

   #parte de gerard 
class Truck(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Activo'),
        ('MAINTENANCE', 'Mantenimiento'),
        ('INACTIVE', 'Inactivo'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    license_plate = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return f"{self.license_plate} - {self.brand} {self.model}"

 #parte de papas
class Route(models.Model):
    STATUS_CHOICES = [
    ('PENDING', 'Pendiente'),
    ('IN_PROGRESS', 'En progreso'),
    ('COMPLETED', 'Completada'),
    ('CANCELLED', 'Cancelada'),
 ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='routes')
    driver = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='routes',
    limit_choices_to={'role': 'DRIVER'}
)
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.origin} → {self.destination} ({self.truck.license_plate})"
    