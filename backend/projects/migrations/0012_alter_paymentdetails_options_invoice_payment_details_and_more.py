# Generated by Django 4.2 on 2023-04-04 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0011_paymentdetails"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paymentdetails",
            options={
                "verbose_name": "Payment Details",
                "verbose_name_plural": "Payment Details",
            },
        ),
        migrations.AddField(
            model_name="invoice",
            name="payment_details",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="projects.paymentdetails",
            ),
        ),
        migrations.AddField(
            model_name="paymentdetails",
            name="status",
            field=models.CharField(
                choices=[
                    ("Paid", "Paid"),
                    ("Pending", "Pending"),
                    ("Failed", "Failed"),
                ],
                default=("Paid", "Paid"),
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]