# Generated by Django 3.2.7 on 2021-09-10 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addmovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movies_name', models.CharField(max_length=25)),
                ('movies_image', models.ImageField(blank=True, null=True, upload_to='UserImage')),
                ('category_types', models.CharField(choices=[('movies', 'movies'), ('webseries', 'webseries'), ('Anime', 'Anime')], max_length=25)),
                ('movies_rating', models.CharField(max_length=25)),
                ('movies_audio', models.CharField(max_length=25)),
                ('movies_intro', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(choices=[('movies', 'movies'), ('webseries', 'webseries'), ('Anime', 'Anime')], max_length=25)),
                ('category_name', models.CharField(max_length=25)),
                ('category_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='moviescounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Counter', models.IntegerField(default=0)),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.addmovies')),
            ],
        ),
        migrations.AddField(
            model_name='addmovies',
            name='movies_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='Test.category'),
        ),
    ]
