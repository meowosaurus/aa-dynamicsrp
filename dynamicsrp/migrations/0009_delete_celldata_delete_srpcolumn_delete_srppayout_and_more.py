# Generated by Django 4.0.10 on 2023-08-12 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicsrp', '0008_cell_column'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CellData',
        ),
        migrations.DeleteModel(
            name='SrpColumn',
        ),
        migrations.DeleteModel(
            name='SrpPayout',
        ),
        migrations.DeleteModel(
            name='SrpShip',
        ),
    ]
