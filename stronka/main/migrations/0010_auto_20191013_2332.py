# Generated by Django 2.2.2 on 2019-10-13 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191013_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='tutorial_summary',
            new_name='category_summary',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 23, 32, 5, 500760), verbose_name='date publishhed'),
        ),
    ]
