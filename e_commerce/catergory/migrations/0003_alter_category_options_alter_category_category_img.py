# Generated by Django 5.2 on 2025-04-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergory', '0002_rename_cat_img_category_category_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_img',
            field=models.ImageField(blank=True, upload_to='photos/category'),
        ),
    ]
