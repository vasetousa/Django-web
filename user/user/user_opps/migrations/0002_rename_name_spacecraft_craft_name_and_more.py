# Generated by Django 4.0.4 on 2022-04-25 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_opps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spacecraft',
            old_name='name',
            new_name='craft_name',
        ),
        migrations.DeleteModel(
            name='RegisterSpaceCraft',
        ),
    ]