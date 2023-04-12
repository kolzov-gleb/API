from .models import Author, Book
from rest_framework import serializers

class AuthorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'year_of_birth']

class BookrSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'year_of_manufacture', 'number_of_pages', 'author']
