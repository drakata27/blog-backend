# Generated by Django 5.0.1 on 2024-03-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blog_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
