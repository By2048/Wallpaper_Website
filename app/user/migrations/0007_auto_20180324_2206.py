# Generated by Django 2.0.3 on 2018-03-24 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180324_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000, verbose_name='消息内容')),
                ('is_read', models.BooleanField(default=False, verbose_name='时候读取')),
                ('date_send', models.DateTimeField(default=django.utils.timezone.now, verbose_name='消息发送时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
                'db_table': 'db_user_message',
            },
        ),
        migrations.RenameField(
            model_name='userauthentication',
            old_name='expired_time',
            new_name='date_expired',
        ),
        migrations.RenameField(
            model_name='userauthentication',
            old_name='send_time',
            new_name='date_send',
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image.Image', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='resource/user_image/default.png', help_text='用户显示的头像！', upload_to='image/%Y/%m', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='发送的用户'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='接受的用户'),
        ),
    ]