# Generated by Django 3.0.7 on 2021-02-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0015_auto_20210205_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='image',
        ),
        migrations.AlterField(
            model_name='patient',
            name='county',
            field=models.TextField(help_text='Enter your county of residence', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='subCounty',
            field=models.TextField(help_text='Enter your county of residence', null=True),
        ),
    ]
