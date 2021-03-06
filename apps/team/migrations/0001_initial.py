# Generated by Django 3.2.9 on 2021-11-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: Кума Кумович', max_length=255, verbose_name='Название')),
                ('position', models.CharField(help_text='Например: Senior Backend developer', max_length=255, verbose_name='Должность')),
                ('description', models.TextField(verbose_name='о себе')),
                ('image', models.ImageField(help_text='Загружайте только jpg и png формат изображении', upload_to='team', verbose_name='Фото')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('department', models.CharField(help_text='Например: Android департамент', max_length=255, verbose_name='Департамент')),
                ('experience', models.CharField(help_text='3 года', max_length=255, verbose_name='Стаж')),
                ('phone', models.CharField(help_text='+996771 771 771', max_length=255, verbose_name='Телефон')),
                ('email', models.CharField(help_text='kuma@gmail.com', max_length=255, verbose_name='email')),
                ('address', models.CharField(help_text='Level 2, 11 York St, Sydney 2000', max_length=255, verbose_name='адрес')),
            ],
            options={
                'verbose_name_plural': 'Команда',
            },
        ),
    ]
