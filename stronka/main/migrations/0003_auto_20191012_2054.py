# Generated by Django 2.2.2 on 2019-10-12 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190928_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 20, 54, 43, 593920), verbose_name='date publishhed'),
        ),
    ]
