# Generated by Django 2.2.6 on 2020-01-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_person_id_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name', 'id_num')},
        ),
        migrations.AddField(
            model_name='person',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='died',
            field=models.DateField(blank=True, null=True),
        ),
    ]
