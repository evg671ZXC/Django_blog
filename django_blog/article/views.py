from django.shortcuts import render
from django.views.generic import View

# from django.http import HttpResponse


# Create your views here.
class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        title = "Эта странница статей блога"
        return render(request, "articles/index.html", context={"title": title})
