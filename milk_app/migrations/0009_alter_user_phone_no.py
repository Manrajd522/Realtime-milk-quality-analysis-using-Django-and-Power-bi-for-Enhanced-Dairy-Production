# Generated by Django 4.0.3 on 2024-05-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk_app', '0008_alter_user_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Phone_No',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
