# Generated by Django 3.1.7 on 2021-03-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0055_auto_20210319_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
