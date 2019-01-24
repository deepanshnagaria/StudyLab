# Generated by Django 2.1.1 on 2019-01-24 19:23

import django.contrib.postgres.fields
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklet',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=jsonfield.fields.JSONField(), size=None),
        ),
        migrations.AlterField(
            model_name='dpp',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=jsonfield.fields.JSONField(), size=None),
        ),
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=jsonfield.fields.JSONField(blank=True, null=True), blank=True, size=None),
        ),
    ]
