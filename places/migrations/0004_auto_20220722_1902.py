# Generated by Django 3.2.10 on 2022-07-22 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
