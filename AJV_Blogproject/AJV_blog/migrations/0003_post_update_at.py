# Generated by Django 5.1.1 on 2024-10-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AJV_blog', '0002_post_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
