# Generated by Django 2.2.6 on 2019-10-22 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_auto_20191022_1517'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
