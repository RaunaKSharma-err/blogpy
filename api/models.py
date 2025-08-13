from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=200)
    released_date = models.IntegerField()

    def __str__(self):
        return f"{self.title}"