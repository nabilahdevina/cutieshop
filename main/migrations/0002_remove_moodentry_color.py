# Generated by Django 5.1.1 on 2024-09-09 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='color',
        ),
    ]
