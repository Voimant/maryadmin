# Generated by Django 5.0.4 on 2024-04-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myurist', '0002_affairs_category_affairs_role_affairs_sub_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='affairs',
            name='nuber_affair',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Номер дела'),
        ),
    ]