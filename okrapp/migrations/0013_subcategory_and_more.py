# Generated by Django 5.0.4 on 2024-05-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okrapp', '0012_checklisttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='checklisttable',
            old_name='category_points_id',
            new_name='sub_cat',
        ),
        migrations.AlterField(
            model_name='checklisttable',
            name='date',
            field=models.DateField(),
        ),
    ]
