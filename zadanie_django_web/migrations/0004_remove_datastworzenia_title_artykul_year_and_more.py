# Generated by Django 5.0 on 2023-12-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadanie_django_web', '0003_datastworzenia_dlugosc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datastworzenia',
            name='title',
        ),
        migrations.AddField(
            model_name='artykul',
            name='year',
            field=models.PositiveSmallIntegerField(default=2023),
        ),
        migrations.AddField(
            model_name='datastworzenia',
            name='Date',
            field=models.PositiveSmallIntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='artykul',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
