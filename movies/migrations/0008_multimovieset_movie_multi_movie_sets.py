# Generated by Django 4.2 on 2023-05-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_release_year_movie_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiMovieSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='multi_movie_sets',
            field=models.ManyToManyField(to='movies.multimovieset'),
        ),
    ]