# Generated by Django 5.1 on 2024-08-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.CharField(max_length=100),
        ),
    ]
