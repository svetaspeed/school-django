from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Review(models.Model):
    vote = models.SmallIntegerField()
    user = models.CharField('Имя', max_length=50)
    text = models.TextField('Отзыв', null=True)
    voted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vote

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

