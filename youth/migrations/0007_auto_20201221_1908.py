# Generated by Django 3.1.4 on 2020-12-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0006_auto_20201221_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
