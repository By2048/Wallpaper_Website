# Generated by Django 2.0.3 on 2018-03-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0004_auto_20180320_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name': '图片得分', 'verbose_name_plural': '图片得分'},
        ),
        migrations.AlterField(
            model_name='userrateing',
            name='point',
            field=models.IntegerField(choices=[(1, '1 星'), (2, '2 星'), (3, '3 星'), (4, '4 星'), (5, '5 星')], verbose_name='得分'),
        ),
    ]
