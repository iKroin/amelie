# Generated by Django 2.2.25 on 2021-12-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20211115_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintcomment',
            name='official',
            field=models.BooleanField(default=False, verbose_name='Comment by Education Committee'),
        ),
    ]