from django.db import models

class Item(models.Model):
    title=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)
    description=models.TextField()

    def __str__(self):
        return self.name
