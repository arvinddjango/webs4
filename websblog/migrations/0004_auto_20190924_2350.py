# Generated by Django 2.2.5 on 2019-09-24 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0003_auto_20190924_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_img',
            field=models.ImageField(blank=True, default='', upload_to='blog_imgage/sub_blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_img1',
            field=models.ImageField(blank=True, default='', upload_to='blog_imgage/sub_blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_title1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_title2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_title3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_title4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_sub_title5',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
