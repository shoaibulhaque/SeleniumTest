from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    # Add new fields as needed:
    phone_number = models.CharField(max_length=20, blank=True)  # Optional phone number
    address = models.TextField(blank=True)  # Optional address
    birth_date = models.DateField(null=True, blank=True)  # Optional birth date

    def __str__(self):
        return self.name
