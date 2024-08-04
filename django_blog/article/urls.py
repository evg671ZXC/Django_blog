from django.urls import path
from django_blog.article import views


urlpatterns = [
    path("", views.index),
    path("<slug:tags>/<int:article_id>", views.article_view, name="article"),
]
