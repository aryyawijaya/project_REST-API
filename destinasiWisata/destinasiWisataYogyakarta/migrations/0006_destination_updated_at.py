# Generated by Django 3.2 on 2021-04-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinasiWisataYogyakarta', '0005_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
