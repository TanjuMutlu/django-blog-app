from django.db import models
from django.db.models.fields import CharField, DateTimeField
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Baslik")
    content = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="Olusturulma Tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Gorsel Ekleyin")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments")
    comment_author = models.CharField(max_length=20,verbose_name="isim")
    comment_content = models.CharField(max_length=150,verbose_name="yorum")
    comment_date = DateTimeField(auto_now_add=True,verbose_name="Olusturulma Tarihi")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']