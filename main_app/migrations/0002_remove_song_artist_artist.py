# Generated by Django 5.1.6 on 2025-03-06 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('album', models.CharField(max_length=100)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.song')),
            ],
        ),
    ]
