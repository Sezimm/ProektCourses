# Generated by Django 3.1.7 on 2021-03-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Science_Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('price_all', models.IntegerField(max_length=20, verbose_name='Цена полный курс')),
                ('price_month', models.IntegerField(max_length=50, verbose_name='Цена за месяц')),
                ('period', models.CharField(max_length=20, verbose_name='Продолжительность курса')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
        ),
        migrations.CreateModel(
            name='Students_Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('age', models.IntegerField(max_length=3, verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers_Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('age', models.IntegerField(max_length=3, verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
        ),
    ]
