# Generated by Django 3.2.3 on 2022-05-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]