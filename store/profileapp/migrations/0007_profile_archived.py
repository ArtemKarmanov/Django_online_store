# Generated by Django 4.2.4 on 2023-08-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0006_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]