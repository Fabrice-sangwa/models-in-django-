# Generated by Django 4.2.1 on 2023-05-30 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blopost_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BloPost',
            new_name='BlogPost',
        ),
    ]
