from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class BookPageNumberPagination(PageNumberPagination):
    page_size = 5
    

class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    

# A cursor is a pointer to a specific item in the list, not an index or page number.
# This method is ideal for large datasets because it avoids the problems of limit/offset pagination, especially when data changes frequently.
class BookCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'  # Specify the field to order by


class BookListPageNumber(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPageNumberPagination


class BookListLimitOffset(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookLimitOffsetPagination


class BookListCursor(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookCursorPagination

    