# Generated by Django 4.0.10 on 2023-08-12 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicsrp', '0021_alter_payout_reimbursement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payout',
            name='ship',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='dynamicsrp.ship'),
        ),
    ]
