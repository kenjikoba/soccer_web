# Generated by Django 3.2.15 on 2022-09-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_data_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.CharField(max_length=200),
        ),
    ]