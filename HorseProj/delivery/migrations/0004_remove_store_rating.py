# Generated by Django 5.0 on 2023-12-09 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_store_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='rating',
        ),
    ]
