# Generated by Django 4.0.3 on 2022-05-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='African', max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(default='John DOE', max_length=300),
        ),
    ]
