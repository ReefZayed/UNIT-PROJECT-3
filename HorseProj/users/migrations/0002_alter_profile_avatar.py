# Generated by Django 5.0 on 2023-12-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/avatar_default.jpg', upload_to='images/'),
        ),
    ]
