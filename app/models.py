from django.db import models


class entry(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField()
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

# Create your models here.
