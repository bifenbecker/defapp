from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", default="Заголовок")
    body = models.TextField(max_length=512, verbose_name="Тело поста", default="")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
