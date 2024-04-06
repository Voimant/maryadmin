from django.db import models

# Create your models here.


class Affairs(models.Model):
    date = models.CharField(max_length=255, verbose_name='Дата решения', null=True, blank=True)
    plaintiff = models.CharField(max_length=255, verbose_name='Истец', null=True, blank=True)
    defendant = models.CharField(max_length=255, verbose_name='Ответчик', null=True, blank=True)
    court = models.CharField(max_length=255, verbose_name='Суд', null=True, blank=True)
    dispute = models.CharField(max_length=255, verbose_name='Суть спора', null=True, blank=True)
    summ_plaintiff = models.CharField(max_length=255, verbose_name='Сумма иска', null=True, blank=True)
    result_client = models.CharField(max_length=255, verbose_name='Сумму отбили/Снизили', null=True, blank=True)
    result_court = models.TextField(max_length=1000, verbose_name='Результат', null=True, blank=True)
    image_result = models.ImageField(upload_to='photo', verbose_name='Фото', null=True, blank=True)
    purist = models.CharField(max_length=255, verbose_name='Ответственный юрист', null=True, blank=True)
    urls = models.CharField(max_length=300, verbose_name='Адрес на дело', null=True, blank=True)
    category = models.CharField(max_length=300, verbose_name='Категория', null=True, blank=True)
    sub_category = models.CharField(max_length=300, verbose_name='Подкатегория', null=True, blank=True)
    role = models.CharField(max_length=300, verbose_name='Моя роль', null=True, blank=True)
    nuber_affair = models.CharField(max_length=300, verbose_name='Номер дела', null=True, blank=True)

    class Meta:
        verbose_name = 'Мои дела'
        verbose_name_plural = 'Мои дела'

    def __str__(self):
        return self.dispute


class Record(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО', null=True, blank=True)
    numbers_phone = models.CharField(max_length=255, verbose_name='Номер телефона', null=True, blank=True)
    dispute = models.CharField(max_length=255, verbose_name='Суть дела', null=True, blank=True)
    username = models.CharField(max_length=255, verbose_name='ТГ', null=True, blank=True)

    class Meta:
        verbose_name = 'Записи на консультацию'
        verbose_name_plural = 'Записи на консультацию'

    def __str__(self):
        return self.name


