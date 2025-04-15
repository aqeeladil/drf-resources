# Viewsets

A ViewSet is like a controller that handles multiple actions (list, retrieve, create, update, delete) in one class — instead of writing many separate views.

Instead of manually defining URL patterns, you can use DRF’s routers to auto-generate them.

You can add your own custom routes inside a ViewSet using @action

## Custom ViewSet Example – GenericViewSet + Mixins

```python
from rest_framework import viewsets, mixins
from .models import Book
from .serializers import BookSerializer

class BookLiteViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

Adding Custom Logic – @action Decorator
```python
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_books = Book.objects.order_by('-published_date')[:5]
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data)
```

## Demo Project

A simple demo project using Django REST Framework that showcases:

- ModelViewSet
- Custom @action
- Routers
- Permissions
- Mixins

**Features:**

- Full CRUD for Book
- Read-only Author
- Custom action: /books/{id}/mark_featured/

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Now visit:

- GET /api/books/
- POST /api/books/
- GET /api/books/{id}/mark_featured/
- GET /api/authors/