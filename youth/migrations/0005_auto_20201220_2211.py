# Generated by Django 3.1.4 on 2020-12-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0004_auto_20201220_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupadmin',
            name='Country',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='groupadmin',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
