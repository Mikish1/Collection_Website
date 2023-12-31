# Generated by Django 4.2.6 on 2023-11-06 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinCollectionApp', '0003_authority_endrule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='obverse_image',
            field=models.ImageField(blank=True, default='Photo', null=True, upload_to='coin_images'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='reverse_image',
            field=models.ImageField(blank=True, default='Photo', null=True, upload_to='coin_images'),
        ),
    ]
