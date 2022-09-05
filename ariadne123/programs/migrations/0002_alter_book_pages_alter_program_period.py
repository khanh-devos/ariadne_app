# Generated by Django 4.1 on 2022-09-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='period',
            field=models.PositiveIntegerField(default=6),
        ),
    ]
