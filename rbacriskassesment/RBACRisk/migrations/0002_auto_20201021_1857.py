# Generated by Django 2.2.12 on 2020-10-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RBACRisk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midpointobjecttype',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
