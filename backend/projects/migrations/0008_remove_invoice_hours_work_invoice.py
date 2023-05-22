# Generated by Django 4.2 on 2023-04-04 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_project_point_of_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="hours",
        ),
        migrations.AddField(
            model_name="work",
            name="invoice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="projects.invoice",
            ),
        ),
    ]
