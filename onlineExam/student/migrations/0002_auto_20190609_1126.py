# Generated by Django 2.1 on 2019-06-09 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('3', 'difficult'), ('2', 'general'), ('1', 'easy')], max_length=10, verbose_name='等级'),
        ),
    ]
