# Generated by Django 5.0.1 on 2024-01-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_remove_employe_fullnamer_remove_employe_moblie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='fullname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
    ]