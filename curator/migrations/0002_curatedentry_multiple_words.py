# Generated by Django 3.1.3 on 2020-11-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curatedentry',
            name='multiple_words',
            field=models.BooleanField(default=False),
        ),
    ]
