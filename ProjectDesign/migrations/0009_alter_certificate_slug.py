# Generated by Django 3.2.5 on 2023-05-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectDesign', '0008_alter_certificate_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
