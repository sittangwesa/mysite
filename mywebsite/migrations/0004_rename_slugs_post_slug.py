# Generated by Django 4.1.2 on 2022-11-17 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0003_post_slugs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slugs',
            new_name='slug',
        ),
    ]
