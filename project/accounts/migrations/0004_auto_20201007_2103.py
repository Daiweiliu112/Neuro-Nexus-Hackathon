# Generated by Django 3.0.5 on 2020-10-07 21:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201007_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gametrain',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Client'),
        ),
        migrations.AlterField(
            model_name='score',
            name='computed_nums',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True), size=1),
        ),
    ]