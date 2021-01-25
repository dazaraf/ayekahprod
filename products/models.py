from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=0, max_digits=11, default=0)

    # def __str__(self):
    #     return self.title
