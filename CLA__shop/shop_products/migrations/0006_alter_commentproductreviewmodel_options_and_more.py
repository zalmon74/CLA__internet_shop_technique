# Generated by Django 4.1 on 2023-02-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0005_commentproductreviewmodel_reviewproductmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentproductreviewmodel',
            options={'verbose_name': 'Комментарий к товару', 'verbose_name_plural': 'Комментарии к товару'},
        ),
        migrations.AlterModelOptions(
            name='reviewproductmodel',
            options={'verbose_name': 'Отзыв к купленному товару', 'verbose_name_plural': 'Отзывы к купленному товару'},
        ),
        migrations.AlterField(
            model_name='reviewproductmodel',
            name='grade',
            field=models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Оценка товара'),
        ),
    ]
