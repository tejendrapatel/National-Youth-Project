# Generated by Django 3.1.4 on 2020-12-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0057_group_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteers',
            name='activatedate',
            field=models.DateField(null=True),
        ),
    ]
