from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    logo = models.ImageField(upload_to="banner", verbose_name="logo")
    keyword = models.CharField(verbose_name="Ключевые слова", max_length=255)
    description = models.TextField(verbose_name="Описание сайта(компании)", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="телефон #1", blank=True, null=True)
    phone2 = models.CharField(max_length=20, verbose_name="телефон #2", blank=True, null=True)
    time_work = models.CharField(max_length=255, verbose_name="время работы")
    day_work = models.CharField(max_length=255, verbose_name="дни работы")
    email = models.CharField(max_length=255, verbose_name="email #1", blank=True, null=True)
    email2 = models.CharField(max_length=255, verbose_name="email #2", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="address")

    facebook = models.CharField(max_length=255, verbose_name="facebook", blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name="instagram", blank=True, null=True)
    telegram = models.CharField(max_length=255, verbose_name="telegram", blank=True, null=True)
    twitter = models.CharField(max_length=255, verbose_name="twitter", blank=True, null=True)
    youtube = models.CharField(max_length=255, verbose_name="youtube", blank=True, null=True)

    def __str__(self):
        return f"{self.title} ||| {self.address}"
    
    class Meta:
        verbose_name_plural = 'Основные настройки'
