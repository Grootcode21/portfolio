# Generated by Django 3.2.11 on 2022-02-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_auto_20220207_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='choose_subject',
            field=models.CharField(choices=[('Data Analysis', 'Data Analysis'), ('Web Development', 'Web Development'), ('Digital Marketing', 'Digital Marketing'), ('Others(Specify)', 'Others(Specify)')], max_length=200, null=True),
        ),
    ]
