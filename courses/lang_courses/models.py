from django.db import models

class Lang_Courses(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    price_all = models.IntegerField(max_length=20, verbose_name='Цена полный курс')
    price_month = models.IntegerField(max_length=50, verbose_name='Цена за месяц')
    period = models.CharField(max_length=20, verbose_name='Продолжительность курса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

class Students_Lang(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.IntegerField(max_length=3, verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=14, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

class Teachers_Lang(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.IntegerField(max_length=3, verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=14, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
