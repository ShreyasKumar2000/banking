# Generated by Django 4.2.5 on 2023-12-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_district_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
