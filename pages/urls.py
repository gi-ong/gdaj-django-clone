from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "pages"

urlpatterns = [
    path("", TemplateView.as_view(template_name="main.html"), name="home"),
    path(
        "branch/isu",
        TemplateView.as_view(template_name="branch/branch_isu.html"),
    ),
    path("intro/branch", views.BranchView.as_view(), name="branch"),
    path("intro/ci", TemplateView.as_view(template_name="intro/intro_ci.html")),
    path("intro", TemplateView.as_view(template_name="intro/intro.html")),
    path("implant/type/", TemplateView.as_view(template_name="imp/imp_type.html")),
    path("implant", TemplateView.as_view(template_name="imp/imp.html")),
    path("align/type/", TemplateView.as_view(template_name="align/align_type.html")),
    path("align", TemplateView.as_view(template_name="align/align.html")),
    path("beauty/1day", TemplateView.as_view(template_name="beauty/beauty_1day.html")),
    path("beauty", TemplateView.as_view(template_name="beauty/beauty.html")),
    path("general/type/", TemplateView.as_view(template_name="gnral/gnral_type.html")),
    path("general", TemplateView.as_view(template_name="gnral/gnral.html")),
]
