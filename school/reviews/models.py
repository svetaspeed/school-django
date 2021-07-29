from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Rating(models.Model):
    vote = models.SmallIntegerField()
    name = models.CharField('Имя', max_length=50)
    text = models.TextField('Отзыв', null=True)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return str(self.vote)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
