# Generated by Django 2.2.3 on 2019-07-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroapp', '0003_auto_20190712_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='gnp',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='country',
            name='gnpld',
            field=models.DecimalField(decimal_places=3, max_digits=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='lifeexpectancy',
            field=models.DecimalField(decimal_places=3, max_digits=80),
        ),
    ]
