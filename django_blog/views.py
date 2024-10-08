from typing import Any
from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hi"] = "Hi!"
        return context


def about(request):
    return render(request, "about.html")
