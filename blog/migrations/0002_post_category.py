# Generated by Django 3.1.5 on 2021-02-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
