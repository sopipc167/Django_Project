# Generated by Django 5.0.3 on 2024-03-27 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quetion_text',
            new_name='question_text',
        ),
    ]
