# Generated by Django 3.1.4 on 2020-12-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0023_medias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medias',
            name='video_Link',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]