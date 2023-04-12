from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from .models import Author, Book
from .serializers import AuthorSerializers, BookrSerializers
from rest_framework.generics import GenericAPIView

class MyPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 5
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Author.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookrSerializers
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Book.objects.all()
        item_author = self.request.query_params.get('author')
        item_name = self.request.query_params.get('name')
        item_pages = self.request.query_params.get('pages')
        if item_author:
            if item_name:
                queryset = queryset.filter(author=item_author, name=item_name)
            else:
                queryset = queryset.filter(author=item_author)
        elif item_name:
            queryset = queryset.filter(name=item_name)
        elif item_pages:
            if item_pages[0] == '<':
                queryset = queryset.filter(number_of_pages__lt=int(item_pages[1:]))
            elif item_pages[0] == '>':
                queryset = queryset.filter(number_of_pages__gt=int(item_pages[1:]))
            elif item_pages[0] == '=':
                queryset = queryset.filter(number_of_pages=int(item_pages[1:]))
        return queryset

