# Generated by Django 4.0.10 on 2023-08-12 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicsrp', '0020_alter_ship_ship_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payout',
            name='reimbursement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='dynamicsrp.reimbursement'),
        ),
    ]
