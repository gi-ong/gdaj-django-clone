from django.urls import path
from django.views.generic import TemplateView

app_name = "pages"

urlpatterns = [
    path("", TemplateView.as_view(template_name="main.html")),
    path(
        "intro/branch/isu",
        TemplateView.as_view(template_name="intro/intro_bnch_isu.html"),
    ),
    path("intro/branch", TemplateView.as_view(template_name="intro/intro_bnch.html")),
    path("intro/ci", TemplateView.as_view(template_name="intro/intro_ci.html")),
    path("intro", TemplateView.as_view(template_name="intro/intro.html")),
    path("implant/type", TemplateView.as_view(template_name="imp/imp_type.html")),
    path("implant", TemplateView.as_view(template_name="imp/imp.html")),
    path("align/type", TemplateView.as_view(template_name="align/align_type.html")),
    path("align", TemplateView.as_view(template_name="align/align.html")),
    path("beauty/1day", TemplateView.as_view(template_name="beauty/beauty_1day.html")),
    path("beauty", TemplateView.as_view(template_name="beauty/beauty.html")),
    path("gnral/type", TemplateView.as_view(template_name="gnral/gnral_type.html")),
    path("gnral", TemplateView.as_view(template_name="gnral/gnral.html")),
]
