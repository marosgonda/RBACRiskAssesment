# Generated by Django 2.2.12 on 2021-02-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RBACRisk', '0008_rbacperm_rbacrole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rbacperm',
            name='rbacRole',
        ),
        migrations.RemoveField(
            model_name='rbacrole',
            name='rbacUser',
        ),
        migrations.AddField(
            model_name='rbacrole',
            name='rbacPerms',
            field=models.ManyToManyField(to='RBACRisk.RBACPerm'),
        ),
        migrations.AddField(
            model_name='rbacuser',
            name='rbacRoles',
            field=models.ManyToManyField(to='RBACRisk.RBACRole'),
        ),
    ]
