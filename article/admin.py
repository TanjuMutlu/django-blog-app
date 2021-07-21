from django.contrib import admin

# Register your models here.
from .models import Article, Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","create_date"]
    list_display_links = ["title","create_date"]
    search_fields=["title"]
    list_filter=["create_date"]
    class Meta:
        model = Article