# Generated by Django 3.2.16 on 2023-02-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-03-03'),
            preserve_default=False,
        ),
    ]