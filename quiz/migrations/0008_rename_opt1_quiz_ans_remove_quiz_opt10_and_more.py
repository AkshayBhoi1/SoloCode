# Generated by Django 4.0.3 on 2022-04-08 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_quiz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='opt1',
            new_name='ans',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt10',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt3',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt4',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt5',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt6',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt7',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt8',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='opt9',
        ),
    ]
