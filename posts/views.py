from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from . import models, forms


class NoticeView(ListView):

    """HomeView Definition"""

    model = models.NoticePost
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 4
    context_object_name = "notices"
    template_name = "posts/notice.html"


class NoticeDetail(DetailView):

    """RoomDetail Definition"""

    model = models.NoticePost
    context_object_name = "notice_detail"
    template_name = "posts/notice_detail.html"


def NoticeSearch(request):

    category = request.GET.get("c", "all")

    filter_args = {}
    if category != "all":
        filter_args["notice_type"] = category

    notices = models.Post.objects.filter(**filter_args)
    return render(request, "posts/notice_search.html", {"notices": notices})


class QnaView(ListView):

    """HomeView Definition"""

    model = models.QnaPost
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 4
    context_object_name = "notices"
    template_name = "posts/qna.html"


class QnaDetail(DetailView):

    """RoomDetail Definition"""

    model = models.QnaPost
    context_object_name = "qna_detail"
    template_name = "posts/qna_detail.html"
