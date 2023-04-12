from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    class Meta:
        ordering = ["name"]
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    year_of_birth = models.DecimalField(decimal_places=0, max_digits=4)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=30)
    isbn = models.CharField(max_length=17, validators=[MinLengthValidator(17)])
    year_of_manufacture = models.DecimalField(decimal_places=0, max_digits=4)
    number_of_pages = models.DecimalField(decimal_places=0, max_digits=8)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
