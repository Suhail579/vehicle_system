from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

# Create your models here.
class Vehicle(models.Model):
    
    FUEL = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    Name = models.CharField(max_length=25)
    Brand = models.CharField()
    Price_Per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fuel_type = models.CharField(choices=FUEL)
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.Name


class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=25)
    customer_phone = models.CharField(max_length=10)
    Start_date = models.DateField(validators=[MinValueValidator(date.today)])
    End_date = models.DateField()
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def clean(self):

        if self.Start_date < timezone.now().date():
            raise ValidationError("Date please check the date")

        if self.End_date <= self.Start_date:
            raise ValidationError("This vehicle not give date")
        
        if Booking.objects.filter(
            vehicle=self.vehicle,
            Start_date__lte=self.End_date,
            End_date__gte=self.Start_date
        ).exclude(pk=self.pk).exists():
            raise ValidationError("This vehicle is already booked.")

    def save(self, *args, **kwargs):
        self.full_clean()

        days = (self.End_date - self.Start_date).days
        self.Total_amount = days * self.vehicle.Price_Per_day

        super().save(*args, **kwargs)

        self.vehicle.Available = False
        self.vehicle.save()

    def __str__(self):
        return self.customer_name