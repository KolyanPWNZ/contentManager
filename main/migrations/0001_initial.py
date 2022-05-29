# Generated by Django 4.0.3 on 2022-05-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('score', models.FloatField(blank=True, verbose_name='Score')),
                ('description', models.TextField(blank=True, max_length=256, verbose_name='Description')),
                ('genre', models.TextField(max_length=100, verbose_name='Genre')),
                ('author', models.TextField(max_length=100, verbose_name='Author')),
                ('comment', models.TextField(blank=True, max_length=100, verbose_name='Comment')),
                ('viewed', models.DateTimeField(blank=True, verbose_name='Viewed')),
            ],
        ),
    ]
