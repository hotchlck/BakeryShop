# Generated by Django 4.2.5 on 2023-10-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
    ]