# Generated by Django 4.0.4 on 2022-04-28 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_pass', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='if_staff',
            new_name='is_staff',
        ),
    ]
