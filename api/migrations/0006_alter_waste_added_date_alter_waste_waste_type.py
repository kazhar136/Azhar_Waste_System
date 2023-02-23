# Generated by Django 4.0.6 on 2023-02-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_waste_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waste',
            name='added_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='waste',
            name='waste_type',
            field=models.CharField(choices=[('SOLID', 'solid waste'), ('LIQUID', 'liquid waste'), ('HAZARDOUS', 'hazardous waste'), ('ORGANIC', 'organic waste')], max_length=100),
        ),
    ]
