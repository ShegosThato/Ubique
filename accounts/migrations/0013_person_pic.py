# Generated by Django 2.2.6 on 2020-01-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_person_id_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pic',
            field=models.ImageField(default='/accounts/static/accounts/person_banner.jpg', upload_to='images/'),
        ),
    ]