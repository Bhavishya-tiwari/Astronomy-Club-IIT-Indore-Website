# Generated by Django 4.0.1 on 2022-02-07 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0012_interview_photo_blog_author_blog_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='Disc',
            new_name='Group',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='Interviewee',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='Video',
        ),
    ]
