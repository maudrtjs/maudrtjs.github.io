# Generated by Django 2.2.5 on 2020-04-25 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200425_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheet',
            old_name='first_interpretation',
            new_name='first_interpretation_date',
        ),
    ]
