# Generated by Django 4.0.3 on 2022-04-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_alter_userdata_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='mname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]