# Generated by Django 4.2.2 on 2023-11-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='price',
            field=models.IntegerField(),
        ),
    ]
