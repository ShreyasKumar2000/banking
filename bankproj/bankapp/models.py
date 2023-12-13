# banking_app/models.py
from django.contrib.auth.models import User
from django.db import models

from django.utils.text import slugify

class District(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or District.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            # Generate a unique slug if it's not set or if it's a duplicate
            self.slug = self.generate_unique_slug(self.name)

        super().save(*args, **kwargs)

    def generate_unique_slug(self, name):
        base_slug = slugify(name)
        slug = base_slug
        counter = 1

        while District.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug
class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.district}"

class Material(models.Model):
    name = models.CharField(max_length=50)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    account_type = models.CharField(max_length=50)
    materials_provide = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name