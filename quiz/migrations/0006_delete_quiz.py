# Generated by Django 4.0.3 on 2022-04-08 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_rename_js_cppquiz_rename_java_cquiz_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]