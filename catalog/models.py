from tkinter.constants import CASCADE

from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="дата последнего изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)

