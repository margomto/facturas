# Generated by Django 3.1.2 on 2020-11-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0008_auto_20201115_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineafactura',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.21, help_text='Indicar el I.V.A en tanto por uno', max_digits=5),
        ),
    ]
