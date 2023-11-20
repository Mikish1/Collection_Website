# Generated by Django 4.2.6 on 2023-11-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinCollectionApp', '0008_coin_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='obverse_image',
            field=models.ImageField(blank=True, null=True, upload_to='coin_images'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='reverse_image',
            field=models.ImageField(blank=True, null=True, upload_to='coin_images'),
        ),
    ]