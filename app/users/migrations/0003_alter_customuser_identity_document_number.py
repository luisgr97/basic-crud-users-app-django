# Generated by Django 3.2.7 on 2021-09-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_sells'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='identity_document_number',
            field=models.IntegerField(),
        ),
    ]
