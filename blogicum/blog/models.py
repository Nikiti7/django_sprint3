from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор', unique=True, blank=False, help_text=(
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'))
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text=('Снимите галочку, чтобы скрыть публикацию.'))
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField('Название места', max_length=256)
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text=('Снимите галочку, чтобы скрыть публикацию.'))
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации', help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(
        "blog.Location",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение")
    category = models.ForeignKey(
        "blog.Category",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория")
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text=('Снимите галочку, чтобы скрыть публикацию.'))
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
