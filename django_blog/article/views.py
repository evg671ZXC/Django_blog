from django.shortcuts import render

# from django.views.generic import View
from django.views import View
from .models import Article

# from django.http import HttpResponse


# Create your views here.
class ArticlesIndexView(View):
    def get(self, request):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={"articles": articles},
        )


# def index(request):
#     return redirect(reverse("article", args=["python", 42]))


# def article_view(request, tags, article_id):
#     return render(
#         request, "articles/index.html", context={"tags": tags, "article_id": article_id}
#     )
