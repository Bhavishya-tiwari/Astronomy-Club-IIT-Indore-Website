# Generated by Django 4.0.1 on 2022-02-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0008_rename_links_profile_git_lin_insta_fb'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedPerson',
            fields=[
                ('auth_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500)),
                ('Email', models.TextField()),
            ],
        ),
    ]
