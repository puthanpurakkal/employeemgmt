# Generated by Django 4.0.5 on 2022-06-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_pick',
            field=models.ImageField(null=True, upload_to='profilepics'),
        ),
    ]