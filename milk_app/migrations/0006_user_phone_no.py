# Generated by Django 4.0.3 on 2024-05-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk_app', '0005_remove_user_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Phone_No',
            field=models.CharField(default=8437824299, max_length=15),
            preserve_default=False,
        ),
    ]
