# Generated by Django 4.0.2 on 2022-03-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0007_pet_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.CharField(default=1, max_length=23),
            preserve_default=False,
        ),
    ]
