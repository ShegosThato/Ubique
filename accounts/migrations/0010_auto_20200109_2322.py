# Generated by Django 2.2.6 on 2020-01-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200109_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='born',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='DateOfBirth',
        ),
    ]
