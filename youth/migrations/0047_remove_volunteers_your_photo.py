# Generated by Django 3.1.4 on 2020-12-28 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0046_remove_jobinternship_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteers',
            name='your_photo',
        ),
    ]
