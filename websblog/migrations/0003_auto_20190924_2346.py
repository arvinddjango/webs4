# Generated by Django 2.2.5 on 2019-09-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_sub_desc',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_desc1',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_desc2',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_desc3',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_desc4',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_desc5',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_img',
            field=models.ImageField(blank=True, default=True, upload_to='blog_imgage/sub_blog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_img1',
            field=models.ImageField(blank=True, default=True, upload_to='blog_imgage/sub_blog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_title',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_title1',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_title2',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_title3',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_title4',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_sub_title5',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
    ]
