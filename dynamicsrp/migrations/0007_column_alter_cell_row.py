# Generated by Django 4.0.10 on 2023-08-12 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicsrp', '0006_row_cell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='cell',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cells', to='dynamicsrp.row'),
        ),
    ]
