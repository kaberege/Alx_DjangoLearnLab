# Generated by Django 5.1.2 on 2024-11-06 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add book'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book')]},
        ),
    ]
