# Generated by Django 3.1.4 on 2020-12-28 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0040_volunteers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobinternship',
            name='date',
        ),
        migrations.RemoveField(
            model_name='jobinternship',
            name='image',
        ),
        migrations.RemoveField(
            model_name='jobinternship',
            name='para',
        ),
    ]
