# Generated by Django 2.2.5 on 2019-12-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0045_gembuyeradvantage_gembuyeradvantagedesc'),
    ]

    operations = [
        migrations.CreateModel(
            name='DscTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsc_title', models.CharField(max_length=101)),
            ],
        ),
        migrations.CreateModel(
            name='DscTitle1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsc_title_heading', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='DscTitle2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsc_title_span', models.CharField(max_length=151)),
            ],
        ),
    ]
