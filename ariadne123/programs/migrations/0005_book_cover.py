# Generated by Django 4.1 on 2022-09-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_alter_book_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.FileField(default='static/images/addimage.png', upload_to='static/images/'),
        ),
    ]