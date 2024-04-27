from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"Color({self.name})"

# Create your models here.
class Item(models.Model):
    name  = models.CharField(max_length=100, verbose_name="vn Имя")
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(default='Начальное описание товара', max_length=200)
    colors = models.ManyToManyField(to=Color)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Item({self.name})"
    
    def display_colors(self):
        return ",".join(color.name for color in self.colors.all())
    
    display_colors.short_discription = "Цвета"