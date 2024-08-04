from django.shortcuts import render, redirect

# from django.views.generic import View
from django.urls import reverse

# from django.http import HttpResponse


# Create your views here.
# class ArticlesIndexView(View):
#     def get(self, request):
# title = "Эта странница статей блога"
# return render(
#     request,
#     "articles/index.html",
#     context={"title": title},
# )
def index(request):
    return redirect(reverse("article", args=["python", 42]))


def article_view(request, tags, article_id):
    return render(
        request, "articles/index.html", context={"tags": tags, "article_id": article_id}
    )
