# Generated by Django 2.2.3 on 2019-09-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actorpic',
            name='apic',
            field=models.URLField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='actresspic',
            name='aspic',
            field=models.URLField(max_length=2000),
        ),
    ]