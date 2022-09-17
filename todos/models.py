from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import pytz


class Distribution(models.Model):
    date_start = models.DateTimeField(db_index=True, verbose_name='Время начала рассылки')
    body = models.TextField(verbose_name='текст сообщения')
    date_finish = models.DateTimeField(db_index=True, verbose_name='Время окончания рассылки')
    tag = models.CharField(max_length=100, verbose_name='тэг клиента')
    code_provider = models.IntegerField(verbose_name='Код оператора клиента')

    def __str__(self):
        return f'Distrubution {self.pk} start at {self.date_start}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_number = PhoneNumberField(verbose_name='Номер телефона',
                                    db_index=True,
                                    unique=True,
                                    help_text='в формате 7XXXXXXXXXX (X - цифра от 0 до 9)')
    code_provider = models.IntegerField(verbose_name='Код оператора')
    tag = models.CharField(max_length=100,  verbose_name='тэг')
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC', verbose_name='часовой пояс')

    def __str__(self):
        return f'CLient {self.phone_number} his tag {self.tag}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    STATUS_SEND = [
        ('SENT', 'Отправлено'),
        ('NOT SENT', 'Не отправлено')
    ]

    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    status_send = models.CharField(
        max_length=30,
        choices=STATUS_SEND,
        db_index=True,
        default='NOT SENT',
        verbose_name='Статус сообщения')
    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE, related_name='message')
    client = models.ManyToManyField(Client, related_name='messages')

    def __str__(self):
        return f'Message -{self.pk}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


# Create your models here.
