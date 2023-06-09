# Generated by Django 4.2 on 2023-04-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0010_invoice_bill_to_company_invoice_bill_to_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vendor",
                    models.CharField(choices=[("Venmo", "Venmo")], max_length=100),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "transaction_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
    ]
