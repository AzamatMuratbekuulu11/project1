# Generated by Django 5.0.6 on 2024-05-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imaeg',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
