# Generated by Django 3.0.1 on 2020-04-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_case'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='coordinates',
            new_name='coordinates_X',
        ),
        migrations.AddField(
            model_name='case',
            name='coordinates_Y',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
