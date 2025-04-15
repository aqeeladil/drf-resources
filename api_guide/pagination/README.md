# Pagination

Pagination is used to split large datasets into smaller, more manageable chunks (pages) so that clients can request data piece by piece, reducing memory usage and improving performance. DRF provides multiple ways to implement pagination, and each has its use case.

- **PageNumberPagination:** Best for simple use cases where you want clients to request a specific page of data.

- **LimitOffsetPagination:** Offers more control to the client, as they can specify how many items to return (limit) and from where to start (offset).

- **CursorPagination:** Ideal for large datasets or when records are added or removed frequently, providing a stable pagination experience.

- **Custom Pagination:** When you need full control over how pagination is represented in the API response, such as nesting pagination links or adding additional metadata.

## Demo Project

It covers the three main pagination styles (PageNumberPagination, LimitOffsetPagination, and CursorPagination). The app will expose an API of books, and we’ll show how to paginate them using different styles.

Add sample books:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db
python manage.py createsuperuser
python manage.py runserver
```

Try it out
`http://127.0.0.1:8000/admin/books/book/`

`http://127.0.0.1:8000/api/books/page-number/`

`http://127.0.0.1:8000/api/books/limit-offset/?limit=5&offset=10`

`http://127.0.0.1:8000/api/books/cursor/`
