# Generated by Django 3.0.4 on 2020-03-31 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200331_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(to='main.Platform'),
        ),
    ]
