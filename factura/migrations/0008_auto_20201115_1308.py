# Generated by Django 3.1.2 on 2020-11-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0007_auto_20201114_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineafactura',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]