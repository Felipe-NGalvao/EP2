from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    title = models.CharField("Título", max_length=255)
    content = models.TextField("Conteúdo (HTML)")
    pub_date = models.DateTimeField("Data de postagem", default=timezone.now)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor"
    )
    text = models.TextField("Comentário")
    pub_date = models.DateTimeField("Data de postagem", default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f"{self.author.username}: {self.text[:30]}"