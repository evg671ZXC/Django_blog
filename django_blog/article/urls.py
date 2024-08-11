from django.urls import path
from django_blog.article import views


urlpatterns = [
    path("", views.ArticlesIndexView.as_view(), name="article"),
    path("<int:id>/", views.ArticleShowView.as_view(), name="article_show"),
    path("create/", views.ArticleFormCreateView.as_view(), name="article_create"),
    path("<int:id>/edit", views.ArticleFormEditView.as_view(), name="article_update"),
    path(
        "<int:id>/delete", views.ArticleFormDeleteView.as_view(), name="article_delete"
    ),
]
