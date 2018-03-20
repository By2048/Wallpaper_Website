# Generated by Django 2.0.3 on 2018-03-20 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image.Image', verbose_name='图片')),
                ('uer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
                'db_table': 'db_favorite',
            },
        ),
    ]
