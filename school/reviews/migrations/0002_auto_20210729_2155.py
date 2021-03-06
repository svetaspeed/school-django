# Generated by Django 3.2.5 on 2021-07-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='image',
        ),
        migrations.AddField(
            model_name='rating',
            name='name',
            field=models.CharField(default='name', max_length=50, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='rating',
            name='text',
            field=models.TextField(null=True, verbose_name='Отзыв'),
        ),
    ]
