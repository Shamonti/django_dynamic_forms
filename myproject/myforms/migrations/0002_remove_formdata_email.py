# Generated by Django 5.0 on 2024-03-28 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myforms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='email',
        ),
    ]
