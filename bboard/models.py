from django.db import models

#объявим модель Bb представляющую объявление с полями..
class Bb(models.Model):
    # ..заголовок объявления с названием продаваемого товара:
    title = models.CharField(max_length=50)
    # сам текст объявления, описание товара:
    content = models.TextField(null=True, blank=True)
    # цена:
    price = models.FloatField(null=True, blank=True)
    # дата публикации
    published = models.DateTimeField(auto_now_add=True, db_index=True)