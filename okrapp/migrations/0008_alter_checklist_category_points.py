# Generated by Django 4.2.11 on 2024-04-18 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okrapp', '0007_checklist_category_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='category_points',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='okrapp.categorypoints'),
        ),
    ]