from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Populate the database with sample Book entries'

    def handle(self, *args, **kwargs):
        created_count = 0

        for i in range(1, 21):
            title = f'Book {i}'
            author = f'Author {i}'
            published_year = 2000 + i

            # Prevent duplication on re-run
            if not Book.objects.filter(title=title).exists():
                Book.objects.create(
                    title=title,
                    author=author,
                    published_year=published_year
                )
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} books.'))
