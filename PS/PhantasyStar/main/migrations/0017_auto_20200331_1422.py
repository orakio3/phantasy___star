# Generated by Django 3.0.4 on 2020-03-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200331_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
