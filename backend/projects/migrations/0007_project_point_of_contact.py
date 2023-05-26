# Generated by Django 4.2 on 2023-04-04 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
        ("projects", "0006_work_billable"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="point_of_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contacts.contact",
            ),
        ),
    ]