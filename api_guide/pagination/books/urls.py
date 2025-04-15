from django.urls import path
from .views import BookListPageNumber, BookListLimitOffset, BookListCursor


urlpatterns = [
    path('page-number/', BookListPageNumber.as_view(), name='book-list-page-number'),
    path('limit-offset/', BookListLimitOffset.as_view(), name='book-list-limit-offset'),
    path('cursor/', BookListCursor.as_view(), name='book-list-cursor'),
]
