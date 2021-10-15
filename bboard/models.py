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

    rubric = models.ForeignKey(
        'Rubric', null=True,
        on_delete=models.PROTECT, verbose_name='Рубрика'
    )

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(
        max_length=20, db_index=True, verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
