# Generated by Django 2.2.5 on 2019-12-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websblog', '0038_whoweare_whoweareabthaving_whoweareabthavingdetails_whowearecompanyvalue_whowearecompanyvalueimppoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='GemTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gem_title', models.CharField(max_length=101)),
            ],
        ),
    ]
