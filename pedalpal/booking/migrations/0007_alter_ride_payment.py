# Generated by Django 4.2.10 on 2024-03-09 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0002_remove_payment_payment_id_payment_id_payment_user"),
        ("booking", "0006_alter_lock_hub"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ride",
            name="payment",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payment.payment",
            ),
        ),
    ]
