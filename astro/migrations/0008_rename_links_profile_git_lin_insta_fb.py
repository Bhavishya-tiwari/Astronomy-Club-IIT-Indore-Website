# Generated by Django 4.0.1 on 2022-01-31 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0007_profile_old'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='links',
            new_name='git_lin_insta_fb',
        ),
    ]
