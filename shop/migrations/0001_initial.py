# Generated by Django 3.0.6 on 2020-06-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('product_type', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('product_image', models.URLField()),
            ],
        ),
    ]
