from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def mark_featured(self, request, pk=None):
        book = self.get_object()
        book.featured = True
        book.save()
        return Response({'status': 'book marked as featured'})

class AuthorViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
