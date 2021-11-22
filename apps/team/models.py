from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например: Кума Кумович"
    )
    position = models.CharField(
        max_length=255, verbose_name="Должность", 
        help_text="Например: Senior Backend developer"
        )
    description = models.TextField(verbose_name="о себе")
    image = models.ImageField(
        upload_to="team", verbose_name="Фото", 
        help_text="Загружайте только jpg и png формат изображении"
    )
    age = models.IntegerField(verbose_name="Возраст")
    department = models.CharField(
        max_length=255, verbose_name="Департамент", help_text="Например: Android департамент"
    )
    experience = models.CharField(max_length=255, verbose_name="Стаж", help_text="3 года")
    phone = models.CharField(max_length=255, verbose_name="Телефон", help_text="+996771 771 771")
    email = models.CharField(max_length=255, verbose_name="email", help_text="kuma@gmail.com")
    address = models.CharField(max_length=255, verbose_name="адрес", help_text="Level 2, 11 York St, Sydney 2000")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Команда'