# Generated by Django 4.0.2 on 2022-02-04 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='shorturl',
            new_name='makeurl',
        ),
    ]