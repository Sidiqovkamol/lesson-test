# Generated by Django 3.1.4 on 2022-05-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='media/book-images'),
        ),
    ]