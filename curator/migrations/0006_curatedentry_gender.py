# Generated by Django 3.1.3 on 2020-11-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curator', '0005_auto_20201105_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='curatedentry',
            name='gender',
            field=models.CharField(choices=[('N', 'Neutre'), ('F', 'Féminin'), ('M', 'Masculin')], default='N', max_length=1),
        ),
    ]
