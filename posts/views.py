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
    title = request.GET.get("q", "")
    filter_args = {}
    if category != "all":
        filter_args["notice_type"] = category
    if title != "":
        filter_args["title__icontains"] = title

    notices = models.NoticePost.objects.filter(**filter_args)
    return render(request, "posts/notice_search.html", {"notices": notices})


class BnAView(ListView):

    """HomeView Definition"""

    model = models.BnAPost
    paginate_by = 9
    ordering = "created"
    context_object_name = "bnas"
    template_name = "posts/beforeafter.html"


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
