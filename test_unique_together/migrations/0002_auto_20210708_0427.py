# Generated by Django 3.1.3 on 2021-07-08 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_unique_together', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tweet',
            unique_together=set(),
        ),
    ]
