from django.urls import path
from django.views.generic import TemplateView

app_name = "posts"

urlpatterns = [
    path("notice", TemplateView.as_view(template_name="posts/notice.html")),
    path(
        "notice/<int:pk>",
        TemplateView.as_view(template_name="posts/notice_detail.html"),
    ),
    path("beforeafter", TemplateView.as_view(template_name="posts/beforeafter.html")),
    path(
        "beforeafter/<int:pk>",
        TemplateView.as_view(template_name="posts/beforeafter_detail.html"),
    ),
    path("qna", TemplateView.as_view(template_name="posts/qna.html")),
    path("qna/write", TemplateView.as_view(template_name="posts/qna_write.html")),
    path("qna/<int:pk>", TemplateView.as_view(template_name="posts/qna_detail.html")),
    path("news", TemplateView.as_view(template_name="posts/news.html")),
    path("news/<int:pk>", TemplateView.as_view(template_name="posts/news_detail.html")),
]
