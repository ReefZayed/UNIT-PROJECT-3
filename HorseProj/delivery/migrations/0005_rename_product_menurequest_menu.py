# Generated by Django 4.2.7 on 2023-12-13 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_alter_store_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menurequest',
            old_name='product',
            new_name='menu',
        ),
    ]
