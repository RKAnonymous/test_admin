# Generated by Django 4.2.7 on 2023-11-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contracts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='usernameM', max_length=50),
        ),
    ]
