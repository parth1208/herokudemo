# Generated by Django 3.2.7 on 2021-09-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_alter_movieslink_moviesname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmovies',
            name='movies_name',
            field=models.CharField(max_length=200),
        ),
    ]