# Generated by Django 5.0.1 on 2024-02-27 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafedra', '0019_rename_slug_for_summary_mainpage_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='summary',
            field=models.FileField(upload_to='static/cafedra/pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]