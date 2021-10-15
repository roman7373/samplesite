from django.db import models

# объявим модель Bb представляющую объявление с полями..


class Bb(models.Model):
    # ..заголовок объявления с названием продаваемого товара:
    title = models.CharField(max_length=50, verbose_name='Товар')
    # сам текст объявления, описание товара:
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    # цена:
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    # дата публикации
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Опубликовано'
    )

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
