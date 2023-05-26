# Generated by Django 4.2 on 2023-04-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_alter_company_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="email",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="phone",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="state",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="website",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="zip_code",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
