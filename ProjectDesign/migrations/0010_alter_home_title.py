# Generated by Django 3.2.5 on 2023-05-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectDesign', '0009_alter_certificate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='title',
            field=models.CharField(default='Shubham Sahu', max_length=20, unique=True),
        ),
    ]