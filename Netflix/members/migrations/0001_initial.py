# Generated by Django 4.0.3 on 2022-05-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rating', models.CharField(max_length=30)),
                ('released', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
