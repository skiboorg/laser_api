from django.db import models

class CallbackForm(models.Model):
    name = models.CharField('Имя',max_length=255,blank=False, null=True)
    company= models.CharField('Наименование компании',max_length=255,blank=False, null=True)
    email= models.CharField('Почта',max_length=255,blank=True, null=True)
    file= models.FileField('Карточка предприятия',upload_to='forms',blank=True, null=True)
    is_done = models.BooleanField('Обработана', default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)