# Generated by Django 4.2.7 on 2023-12-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=True),
        ),
    ]
