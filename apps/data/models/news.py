from django.db import models
from pytils.translit import slugify
from django_ckeditor_5.fields import CKEditor5Field

class NewsItem(models.Model):
    page_title = models.TextField("TITLE", blank=True, null=True)
    page_description = models.TextField("DESCRIPTION", blank=True, null=True)
    order_num = models.IntegerField(default=1, null=True)
    cover = models.ImageField('Картинка превью', upload_to='news/images',blank=False, null=True)

    name = models.CharField('Название', max_length=255, blank=False, null=True)
    short_description = models.TextField('Короткое описание',blank=True, null=True)
    slug = models.CharField('ЧПУ',max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    content = CKEditor5Field(verbose_name='Редактор', blank=True, config_name='extends')
    show_on_main = models.BooleanField("Показывать на главной", default=False)
    tags = models.TextField(blank=True, verbose_name='Тэги (через запятую)', null=True)
    created = models.DateField(blank=True, null=True)

    photo = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Фото человека')
    full_name = models.CharField(max_length=255,blank=True, null=True,  verbose_name='ФИО')
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='Подпись к ФИО')



    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def tags_list(self):
        """Возвращает список тэгов"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

class Image(models.Model):
    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE, related_name='images')
    image = models.FileField('Картинка', upload_to='news/images', blank=False, null=True)