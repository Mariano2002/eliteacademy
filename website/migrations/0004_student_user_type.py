# Generated by Django 3.2.7 on 2021-10-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_prenotime'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_type',
            field=models.CharField(default='normal', max_length=100),
        ),
    ]
