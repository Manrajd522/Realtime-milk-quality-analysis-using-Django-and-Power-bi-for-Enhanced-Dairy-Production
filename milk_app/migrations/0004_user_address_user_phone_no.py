# Generated by Django 4.0.3 on 2024-05-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk_app', '0003_alter_record_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Address',
            field=models.CharField(default=8437824299, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Phone_No',
            field=models.IntegerField(default=8437824299, max_length=10),
            preserve_default=False,
        ),
    ]
