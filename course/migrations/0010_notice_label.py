# Generated by Django 3.2.11 on 2022-05-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20220506_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='标签'),
        ),
    ]
