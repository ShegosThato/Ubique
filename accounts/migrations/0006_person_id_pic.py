# Generated by Django 2.2.6 on 2020-01-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200108_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id_pic',
            field=models.ImageField(default='/home/cj/Documents/dev/pyland/ubiquedumy.png', upload_to='media/<django.db.models.fields.PositiveIntegerField>'),
        ),
    ]
