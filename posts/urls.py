from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "posts"

urlpatterns = [
    # path("notice", TemplateView.as_view(template_name="posts/notice.html")),
    path("notice", views.NoticeView.as_view(), name="notice"),
    path("notice/search", views.NoticeSearch, name="notice_search"),
    path(
        "notice/<int:pk>",
        views.NoticeDetail.as_view(),
        name="notice_detail",
    ),
    path("beforeafter", TemplateView.as_view(template_name="posts/beforeafter.html")),
    path(
        "beforeafter/<int:pk>",
        TemplateView.as_view(template_name="posts/beforeafter_detail.html"),
    ),
    path("qna", views.QnaView.as_view(), name="qna"),
    path("qna/write", TemplateView.as_view(template_name="posts/qna_write.html")),
    path("qna/<int:pk>", views.QnaDetail.as_view(), name="qna_detail"),
    path("news", TemplateView.as_view(template_name="posts/news.html")),
    path("news/<int:pk>", TemplateView.as_view(template_name="posts/news_detail.html")),
]
