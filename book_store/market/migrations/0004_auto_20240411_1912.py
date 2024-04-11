# Generated by Django 3.2 on 2024-04-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_book_discription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name', 'price', 'page_count', 'author_name'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Book Name'),
        ),
    ]