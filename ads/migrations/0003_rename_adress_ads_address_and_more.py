# Generated by Django 4.2.1 on 2023-05-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ads_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='ads',
            old_name='is_public',
            new_name='is_published',
        ),
    ]
