# Generated by Django 5.0.6 on 2024-05-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='day_note',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
    ]
