# Generated by Django 3.2.9 on 2021-11-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0004_synthmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synthmodel',
            name='name',
            field=models.CharField(max_length=16, null=True),
        ),
    ]