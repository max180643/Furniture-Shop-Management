# Generated by Django 3.0.5 on 2020-04-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20200426_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('PURCHASING_OFFICER', 'PURCHASING_OFFICER'), ('SALE_OFFICER', 'SALE_OFFICER')], max_length=18),
        ),
    ]
