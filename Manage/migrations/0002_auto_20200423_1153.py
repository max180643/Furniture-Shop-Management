# Generated by Django 3.0.5 on 2020-04-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
