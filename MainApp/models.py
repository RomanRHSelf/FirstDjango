from django.db import models

# Create your models here.
class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(default='Начальное описание товара', max_length=200)

    def __repr__(self) -> str:
        return f"таблица Item"