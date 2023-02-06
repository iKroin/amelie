# Generated by Django 3.2.16 on 2023-02-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_add_default_career_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelevisionVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('video_id', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Television Promotion Video',
                'verbose_name_plural': 'Television Promotion Videos',
                'ordering': ['-start_date'],
            },
        ),
    ]