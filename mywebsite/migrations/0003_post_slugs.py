# Generated by Django 4.1.2 on 2022-11-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slugs',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
