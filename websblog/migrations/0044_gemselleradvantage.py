# Generated by Django 2.2.5 on 2019-12-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0043_gemsellerregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='GemSellerAdvantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advantage_title', models.CharField(max_length=251)),
            ],
        ),
    ]
