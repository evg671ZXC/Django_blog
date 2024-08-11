# from django.views.generic import View
from django.views import View
from .models import Article
from .forms import ArticleForm

# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


# Create your views here.
class ArticlesIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={"articles": articles},
        )


class ArticleShowView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            "articles/create.html",
            context={
                "form": form,
            },
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно создана!")
            return redirect("article")
        messages.error(request, str(form.errors))
        return render(
            request,
            "articles/create.html",
            context={
                "form": form,
            },
        )


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            "articles/update.html",
            {
                "form": form,
                "article_id": article_id,
            },
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.info(request, "Статья обновлена!")
            return redirect("article")
        return render(
            request,
            "articles/update.html",
            {
                "form": form,
                "article_id": article_id,
            },
        )


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.warning(request, "Статья удалена")
        return redirect("article")
