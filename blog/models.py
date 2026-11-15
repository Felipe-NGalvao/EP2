from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField("Título", max_length=255)
    content = models.TextField("Conteúdo (HTML)")
    pub_date = models.DateTimeField("Data de postagem", default=timezone.now)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title