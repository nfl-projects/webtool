# Generated by Django 2.1.5 on 2019-07-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leagues',
            name='alt_league_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]