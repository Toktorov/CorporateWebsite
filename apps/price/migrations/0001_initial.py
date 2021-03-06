# Generated by Django 3.2.9 on 2021-11-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: Тариф Алилуя', max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(help_text='Например: 46$ / за месяц', max_length=100, verbose_name='Цена')),
            ],
            options={
                'verbose_name_plural': 'Цена',
            },
        ),
    ]
