# Generated by Django 3.1.2 on 2021-10-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20211005_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly')], default=2, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habit',
            name='habit_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]