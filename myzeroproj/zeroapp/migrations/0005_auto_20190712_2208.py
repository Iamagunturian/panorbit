# Generated by Django 2.2.3 on 2019-07-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroapp', '0004_auto_20190712_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='gnpld',
            field=models.DecimalField(decimal_places=3, max_digits=40),
        ),
    ]
