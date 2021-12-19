# Generated by Django 3.2.10 on 2021-12-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211212_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='badge_color',
            field=models.CharField(blank=True, choices=[('bg-primary', 'Blue'), ('bg-secondary', 'Grey'), ('bg-success', 'Green'), ('bg-danger', 'Red'), ('bg-warning ', 'Yellow'), ('bg-info', 'Turquoise')], default='bg-primary', max_length=200, null=True),
        ),
    ]