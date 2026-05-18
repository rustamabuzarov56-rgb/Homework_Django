from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name="заголовок")
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="blog/", blank=True, null=True, verbose_name="превью")
    created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="количество просмотров")

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ['-created_at']  # Свежие статьи будут сверху

    def __str__(self):
        return self.title