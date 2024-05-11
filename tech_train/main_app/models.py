from django.db import models


class Business(models.Model):
    # Auto-incrementing primary key
    id = models.AutoField(primary_key=True)

    # Name of the company
    name = models.CharField(max_length=255)

    # Description
    description = models.TextField(blank=True, null=True)

    # Address
    address = models.CharField(max_length=255, blank=True, null=True)

    # Phone number
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
