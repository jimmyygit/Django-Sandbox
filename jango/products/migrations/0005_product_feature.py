# Generated by Django 3.0.8 on 2020-07-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_agree'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
