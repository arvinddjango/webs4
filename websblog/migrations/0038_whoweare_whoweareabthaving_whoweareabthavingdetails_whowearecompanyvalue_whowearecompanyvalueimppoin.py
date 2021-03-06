# Generated by Django 2.2.5 on 2019-12-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0037_applicationdesign_applicationdesignui_ourdesignberief_socialmedia_socialmediaimg_solutiondesign_solu'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoWeAre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=101)),
                ('heading', models.CharField(max_length=151)),
                ('desc', models.TextField()),
                ('about_img1', models.ImageField(upload_to='who_we_are_img')),
                ('about_img2', models.ImageField(upload_to='who_we_are_img')),
                ('about_img3', models.ImageField(upload_to='who_we_are_img')),
                ('about_img4', models.ImageField(upload_to='who_we_are_img')),
                ('about_img5', models.ImageField(upload_to='who_we_are_img')),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreAbtHaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_having_title', models.CharField(max_length=151)),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreAbtHavingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_having_details_img', models.ImageField(upload_to='who_we_are_img/abt_having_details_img')),
                ('abt_having_details_head', models.CharField(max_length=151)),
                ('abt_having_details_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreCompanyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_company_value_img', models.ImageField(upload_to='who_we_are_img/abt_company_value_img')),
                ('abt_company_value_title', models.CharField(max_length=151)),
                ('abt_company_value_head', models.CharField(max_length=151)),
                ('abt_company_value_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreCompanyValueImpPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_com_value_imp_pt', models.CharField(max_length=151)),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreCultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cul_title', models.CharField(max_length=101)),
                ('cul_head', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreCulturalImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cul_img', models.ImageField(upload_to='who_we_are_img/cul_img')),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreDesinProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_process_img', models.ImageField(upload_to='who_we_are_img/dev_process_img')),
                ('dev_process_title', models.CharField(max_length=101)),
                ('dev_process_head', models.CharField(max_length=151)),
                ('dev_process_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=101)),
                ('work_head', models.CharField(max_length=151)),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAreWorkAbt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_work_img', models.ImageField(upload_to='who_we_are_img/work_img')),
                ('abt_wrok_title', models.CharField(max_length=151)),
                ('abt_work_desc', models.TextField()),
            ],
        ),
    ]
