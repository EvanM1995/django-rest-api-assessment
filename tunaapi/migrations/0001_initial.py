# Generated by Django 4.1.3 on 2023-12-09 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('length', models.DurationField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='tunaapi.artist')),
            ],
        ),
        migrations.CreateModel(
            name='SongGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_genres', to='tunaapi.genre')),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='tunaapi.song')),
            ],
        ),
    ]
