# Generated by Django 4.2.6 on 2024-01-25 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimsontool', '0002_imgclassifierdisplay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imgclassifierdisplay',
            old_name='ImagePath',
            new_name='Image',
        ),
    ]
