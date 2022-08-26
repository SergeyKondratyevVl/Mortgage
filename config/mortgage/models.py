from django.db import models

class Mortgage(models.Model):

    bank_name = models.CharField(max_length=100, verbose_name='Название банка')
    term_min = models.PositiveIntegerField(verbose_name='Срок ипотеки, ОТ')
    term_max = models.PositiveIntegerField(verbose_name='Срок ипотеки, ДО')
    rate_min = models.FloatField(verbose_name='Ставка, ОТ')
    rate_max = models.FloatField(verbose_name='Ставка, ДО')
    payment_min = models.PositiveIntegerField(verbose_name='Сумма кредита, ОТ')
    payment_max = models.PositiveIntegerField(verbose_name='Сумма кредита, ДО')
    