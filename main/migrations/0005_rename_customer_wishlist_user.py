# Generated by Django 5.0.3 on 2024-03-20 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_customer_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='customer',
            new_name='user',
        ),
    ]