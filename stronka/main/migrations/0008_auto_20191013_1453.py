# Generated by Django 2.2.2 on 2019-10-13 12:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191013_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='turorial_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 13, 14, 53, 12, 109506), verbose_name='date publishhed'),
        ),
    ]