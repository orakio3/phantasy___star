# Generated by Django 3.0.4 on 2020-03-31 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200327_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['title']},
        ),
    ]
