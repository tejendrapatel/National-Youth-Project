# Generated by Django 3.1.4 on 2020-12-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0009_auto_20201221_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(null=True, upload_to='')),
                ('para', models.CharField(max_length=200)),
            ],
        ),
    ]