from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "title": "Home - Главная",
            "content": "Магазин мебели HOME",
        }
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "title": "Home - О нас",
            "content": "О нас",
            "text_on_page": "Текст о том почему этот  магазин такой класный и какой хороший товар.",
        }
        return context
