# Generated by Django 4.2.6 on 2023-11-07 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoinCollectionApp', '0005_authority_authority_slug_category_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authority',
            name='authority_slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_slug',
        ),
        migrations.RemoveField(
            model_name='city',
            name='ciy_slug',
        ),
    ]