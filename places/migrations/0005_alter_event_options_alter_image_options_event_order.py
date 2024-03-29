# Generated by Django 4.1 on 2022-08-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220722_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-event',)},
        ),
        migrations.AddField(
            model_name='event',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
