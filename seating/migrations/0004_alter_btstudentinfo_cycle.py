# Generated by Django 4.1.7 on 2023-04-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0003_alter_btstudentinfo_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btstudentinfo',
            name='Cycle',
            field=models.IntegerField(choices=[(10, 'PHYSICS'), (9, 'CHEMISTRY')], default=0),
        ),
    ]