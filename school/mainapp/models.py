from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
