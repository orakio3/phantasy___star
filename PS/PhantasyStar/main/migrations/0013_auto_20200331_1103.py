# Generated by Django 3.0.4 on 2020-03-31 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200331_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='platform',
            options={'ordering': ['title']},
        ),
    ]
