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
    path("beforeafter", views.BnAView.as_view(), name="bna"),
    path("beforeafter/search", views.BnASearch, name="bna_search"),
    path(
        "beforeafter/<int:pk>",
        views.BnADetail.as_view(),
        name="bna_detail",
    ),
    path("qna", views.QnaView.as_view(), name="qna"),
    path("qna/check", views.QnaCheckView, name="qna_check"),
    path("qna/create", views.CreateQnaView.as_view(), name="qna_create"),
    path("qna/<int:pk>", views.QnaDetail.as_view(), name="qna_detail"),
    path(
        "qna/<int:pk>/a_create",
        views.CreateQnaAnswerView.as_view(),
        name="qna_a_create",
    ),
    path("qna/<int:pk>/a_delete", views.qna_a_delete, name="qna_a_delete"),
    path("qna/<int:pk>/a_edit", views.QnaAnswerEditView.as_view(), name="qna_a_edit"),
    path("news", views.NewsView.as_view(), name="news"),
    path(
        "news/<int:pk>",
        views.NewsDetail.as_view(),
        name="news_detail",
    ),
]
