from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):
        from_whom = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='from_whom',
                                  verbose_name='Сообщение')

        to_whom = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='whom_messages',
                                 verbose_name='Сообщение')
        text_message = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Текст сообщения')
        created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

        def __str__(self):
            return f'{self.from_whom} - {self.to_whom}'

        class Meta:
            verbose_name = 'Сообщение'
            verbose_name_plural = 'Сообщения'
