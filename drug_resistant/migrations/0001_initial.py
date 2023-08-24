# Generated by Django 4.1.4 on 2023-02-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genes', models.CharField(max_length=2000, null=True)),
                ('medicine', models.CharField(max_length=255, null=True)),
                ('tf', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
