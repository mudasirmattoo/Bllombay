# Generated by Django 5.1.1 on 2024-09-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.CharField(default=5, max_length=10),
            preserve_default=False,
        ),
    ]
