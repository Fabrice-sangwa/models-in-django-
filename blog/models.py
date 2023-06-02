from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    publish = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    def publibhed_string(self):
        if self.publish:
            return "Cet article est publié"
        return "Cet article n'est pas publié"

    def save(self, *args, **kwargs):
        if len(self.title) == 0:
            self.slug = ""
        elif not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

