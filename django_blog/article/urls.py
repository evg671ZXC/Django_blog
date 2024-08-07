from django.urls import path
from django_blog.article import views


urlpatterns = [
    path("", views.ArticlesIndexView.as_view()),
    path("<int:id>/", views.ArticleShowView.as_view(), name="article_show"),
]
