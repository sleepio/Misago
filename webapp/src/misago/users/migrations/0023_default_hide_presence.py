# Generated by Django 2.2.12 on 2021-02-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misago_users', '0022_deleteduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_hiding_presence',
            field=models.BooleanField(default=True),
        ),
    ]
