# Generated by Django 2.2.5 on 2019-10-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0008_indexservicelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
                ('state_name', models.CharField(max_length=50)),
                ('office_address', models.CharField(max_length=200)),
                ('adress_url', models.CharField(max_length=500)),
                ('address_created_date', models.DateTimeField(auto_now_add=True)),
                ('address_updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
