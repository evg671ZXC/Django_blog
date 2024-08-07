from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    list_filter = (("created_at", admin.DateFieldListFilter),)
    search_fields = ["name", "body"]
