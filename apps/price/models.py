from django.db import models

class Price(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например: Тариф Алилуя"
    )
    description = models.TextField(verbose_name="Описание")
    price = models.CharField(
        max_length=100, verbose_name="Цена", help_text="Например: 46$ / за месяц"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Цена'