# Generated by Django 4.1.2 on 2022-11-13 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
