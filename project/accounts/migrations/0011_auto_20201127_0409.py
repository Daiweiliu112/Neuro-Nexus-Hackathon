# Generated by Django 3.0.5 on 2020-11-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_voice_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='voice_record',
            name='correct',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='voice_record',
            name='incorrect',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
