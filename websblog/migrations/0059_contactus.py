# Generated by Django 2.2.5 on 2019-12-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0058_auto_20191226_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_heading', models.CharField(max_length=151)),
                ('contact_title', models.TextField()),
                ('contact_form_img', models.ImageField(upload_to='contact_us_img/')),
                ('contact_addres', models.CharField(max_length=501)),
                ('contact_num', models.IntegerField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_map', models.CharField(max_length=5000)),
            ],
        ),
    ]
