# Generic Views

Django REST Framework (DRF) provides generic views to save time and avoid repeating code. These are class-based views that are pre-configured for common use cases like listing objects, creating new objects, updating existing objects, and deleting objects.

By using generic views, you can quickly implement basic CRUD operations without writing redundant code.

## Mixins

Mixins are useful for providing behavior across multiple views without repeating code. DRF provides several useful mixins that can be combined with GenericAPIView.

## Demo Project

A small To-Do List API for managing tasks:

- Create a task
- View all tasks
- Retrieve a single task
- Update a task
- Delete a task

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```