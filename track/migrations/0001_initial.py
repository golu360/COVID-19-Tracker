# Generated by Django 3.0.1 on 2020-04-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(blank=True, max_length=100)),
                ('district_positive', models.IntegerField()),
                ('district_tested', models.IntegerField()),
                ('district_recovered', models.IntegerField()),
                ('district_quarantined', models.IntegerField()),
                ('district_deaths', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
