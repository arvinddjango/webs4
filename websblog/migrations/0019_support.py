# Generated by Django 2.2.5 on 2019-11-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0018_developmentprocess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support_desc', models.TextField()),
                ('support_image', models.ImageField(upload_to='support_img/')),
                ('support_contact_name', models.CharField(max_length=51)),
                ('support_contact_designation', models.CharField(max_length=51)),
                ('support_contact_title', models.CharField(max_length=251)),
                ('support_contact_image', models.ImageField(upload_to='support_img/contact_img')),
                ('support_contact_name1', models.CharField(max_length=51)),
                ('support_contact_designation1', models.CharField(max_length=51)),
                ('support_contact_title1', models.CharField(max_length=251)),
                ('support_contact_image1', models.ImageField(upload_to='support_img/contact_img')),
                ('support_created_date', models.DateTimeField(auto_now_add=True)),
                ('support_updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]