# Generated by Django 3.1.6 on 2021-02-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RBACRisk', '0021_rbacperm_oid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbacperm',
            name='type',
            field=models.CharField(blank=True, choices=[('AUT', 'Authorization'), ('ASS', 'Assignment'), ('IDU', 'Inducement')], max_length=3),
        ),
    ]
