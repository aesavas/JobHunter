# Generated by Django 3.2.10 on 2021-12-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skill_image',
        ),
        migrations.AddField(
            model_name='skill',
            name='badge_color',
            field=models.CharField(blank=True, choices=[('bg-primary', 'Blue'), ('bg-secondary', 'Grey'), ('bg-success', 'Green'), ('bg-danger', 'Red'), ('bg-warning ', 'Yellow'), ('bg-info', 'Turquoise')], max_length=200, null=True),
        ),
    ]
