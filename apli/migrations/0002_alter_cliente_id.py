# Generated by Django 4.2.2 on 2023-06-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]