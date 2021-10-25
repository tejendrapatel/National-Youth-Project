# Generated by Django 3.1.4 on 2020-12-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0015_auto_20201222_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(null=True, upload_to='')),
                ('para', models.CharField(max_length=10000)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]