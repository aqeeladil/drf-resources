from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    # email = models.EmailField(max_length=200)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
