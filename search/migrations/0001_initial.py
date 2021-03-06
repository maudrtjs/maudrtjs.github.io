# Generated by Django 2.2.5 on 2020-04-19 18:24

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(default='unknown', max_length=100)),
                ('compositor', models.CharField(default='unknown', max_length=42)),
                ('instrumentation', models.CharField(default='unknown', max_length=155)),
                ('pdf_link', models.URLField(default='unknown')),
                ('sections', models.CharField(default='unknown', max_length=100)),
                ('description', models.CharField(default='unknown', max_length=100)),
                ('composition_date', models.IntegerField(default=0)),
                ('first_interpretation', models.CharField(default='unknown', max_length=100)),
                ('release_date', models.CharField(default='unknown', max_length=100)),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
                ('compositor_period', models.CharField(default='unknown', max_length=100)),
                ('style', models.CharField(default='unknown', max_length=100)),
                ('key', models.CharField(default='unknown', max_length=100)),
                ('source', models.CharField(default='unknown', max_length=100)),
                ('comments', models.CharField(default='no comment', max_length=1000)),
                ('difficulty', models.FloatField(default=0)),
                ('popularity', models.FloatField(default=0)),
                ('dedication', models.CharField(default='unknown', max_length=100)),
                ('num_opus', models.CharField(default='unknown', max_length=100)),
                ('download_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Publication date')),
            ],
            options={
                'verbose_name': 'Music sheets',
                'ordering': ['title'],
            },
        ),
    ]
