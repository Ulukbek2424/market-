from django.db import models
from django.urls import reverse

class Category(models.Model):
    '''Категории каталога'''
    name = models.CharField(max_length=50, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    '''Подкатегории каталога'''
    name = models.CharField(max_length=50, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'category_id': self.category.pk, 'subcategory_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    '''Товар'''
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    description = models.TextField(verbose_name="Описание товара")
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Подкатегория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
