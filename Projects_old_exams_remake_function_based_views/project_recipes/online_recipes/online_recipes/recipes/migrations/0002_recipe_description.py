# Generated by Django 4.0.3 on 2022-04-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
