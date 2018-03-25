# Generated by Django 2.0.3 on 2018-03-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20180322_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.CharField(choices=[('jpg', 'JPG 图片'), ('png', 'PNG 图片'), ('gif', 'GIF 图片'), ('bmp', 'BMP 图片'), ('svg', 'SVG 图片')], max_length=10, verbose_name='图片格式'),
        ),
    ]