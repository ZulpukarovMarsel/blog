from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_delete
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    video = models.FileField(upload_to='blog/video/', verbose_name="Видео")
    title = models.CharField(max_length=150, verbose_name="Загаловок")
    description = models.TextField(verbose_name="Описание")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    tags = models.ManyToManyField(Tag, related_name="blogs", verbose_name="Теги")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

@receiver(pre_delete, sender=Blog)
def delete_blog_video(sender, instance, **kwargs):
    instance.video.delete()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="")
    text = models.TextField(verbose_name="")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="")

    def __str__(self):
        return f"Блог - {self.blog.title} | автор - {self.user.email} | текст - {self.text}"

    class Meta:
        verbose_name = "Комментария"
        verbose_name_plural = "Комментарии"


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="")

    def __str__(self):
        return f"Блог - {self.blog.title} | Автор - {self.user.email}"
    
    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"