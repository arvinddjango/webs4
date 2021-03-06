# Generated by Django 2.2.5 on 2019-12-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0042_gembreif'),
    ]

    operations = [
        migrations.CreateModel(
            name='GemSellerRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_head', models.CharField(max_length=51)),
                ('gem_title_reg', models.CharField(max_length=51)),
                ('gem_seller_desc', models.TextField()),
                ('gem_seller_contact', models.CharField(max_length=251)),
                ('gem_seller_contact_no', models.CharField(max_length=251)),
                ('gem_seller_advantage', models.CharField(max_length=251)),
                ('gem_seller_advantage_title', models.CharField(max_length=251)),
            ],
        ),
    ]
