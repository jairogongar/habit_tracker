# Generated by Django 3.1.2 on 2021-10-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='streak',
            field=models.IntegerField(default=0),
        ),
    ]
