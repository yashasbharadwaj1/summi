# Generated by Django 4.0.4 on 2022-05-14 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_createdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Createdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
