# Generated by Django 4.2.6 on 2023-11-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinCollectionApp', '0006_remove_authority_authority_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='startRule',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
