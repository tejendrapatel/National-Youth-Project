# Generated by Django 3.1.4 on 2020-12-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0016_press'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
