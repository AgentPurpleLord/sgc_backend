# Generated by Django 3.0.5 on 2020-04-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
