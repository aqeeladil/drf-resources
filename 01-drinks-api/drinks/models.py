from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    # image = models.ImageField(upload_to='drinks/')

    def __str__(self):
        return self.name + " - " + str(self.price)
