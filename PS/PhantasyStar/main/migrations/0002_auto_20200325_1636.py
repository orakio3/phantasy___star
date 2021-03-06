# Generated by Django 3.0.4 on 2020-03-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'JRPG'), (1, 'Action-RPG'), (2, 'MMORPG')])),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='faq',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Sega'), (1, 'Sony Playstation'), (2, 'Sony Playstation 2'), (3, 'Sony Playstation 3'), (4, 'X-Box 360'), (5, 'PC')], null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='release',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='summary',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
