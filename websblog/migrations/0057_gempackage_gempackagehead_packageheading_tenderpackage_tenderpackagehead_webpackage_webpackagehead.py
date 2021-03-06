# Generated by Django 2.2.5 on 2019-12-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0056_bidparticiaptionhead'),
    ]

    operations = [
        migrations.CreateModel(
            name='GemPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gem_package_title', models.CharField(max_length=25)),
                ('gem_package_price', models.IntegerField()),
                ('gem_package_title_list1', models.CharField(blank=True, max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='GempackageHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gem_head', models.CharField(max_length=151)),
                ('gem_title', models.CharField(max_length=351)),
            ],
        ),
        migrations.CreateModel(
            name='packageHeading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_title', models.CharField(max_length=55)),
                ('pack_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TenderPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_package_title', models.CharField(max_length=25)),
                ('tender_package_price', models.IntegerField()),
                ('tender_package_title_list1', models.CharField(blank=True, max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='TenderpackageHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_head', models.CharField(max_length=151)),
                ('tender_title', models.CharField(max_length=351)),
            ],
        ),
        migrations.CreateModel(
            name='WebPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_package_title', models.CharField(max_length=25)),
                ('web_package_price', models.IntegerField()),
                ('web_package_title_list1', models.CharField(blank=True, max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='WebpackageHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_head', models.CharField(max_length=151)),
                ('web_title', models.CharField(max_length=351)),
            ],
        ),
    ]
