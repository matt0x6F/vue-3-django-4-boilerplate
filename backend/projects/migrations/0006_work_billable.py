# Generated by Django 4.2 on 2023-04-04 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_invoice_delivered_on_invoice_paid_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="work",
            name="billable",
            field=models.BooleanField(default=True),
        ),
    ]