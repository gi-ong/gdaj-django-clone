from django.views.generic import FormView, ListView, DetailView, UpdateView
from django.shortcuts import redirect, render, reverse
from . import models, forms
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
import json
from django.contrib import messages


class NoticeView(ListView):

    """NoticeView Definition"""

    model = models.NoticePost
    paginate_by = 10
    ordering = "-created"
    context_object_name = "notices"
    template_name = "posts/notice.html"

    def get_context_data(self, **kwargs):
        context = super(NoticeView, self).get_context_data()
        page = context["page_obj"]
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(
            page.number, on_each_side=3, on_ends=0
        )
        context["pagelist"] = pagelist
        return context


class NoticeDetail(DetailView):

    """NoticeDetail Definition"""

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


def BnASearch(request):

    title = request.GET.get("q", "")
    filter_args = {}
    if title != "":
        filter_args["title__icontains"] = title

    bnas = models.BnAPost.objects.filter(**filter_args)
    return render(request, "posts/beforeafter.html", {"bnas": bnas})


class BnAView(ListView):

    """BnaView Definition"""

    model = models.BnAPost
    paginate_by = 9
    ordering = "-created"
    context_object_name = "bnas"
    template_name = "posts/beforeafter.html"

    def get_context_data(self, **kwargs):
        context = super(BnAView, self).get_context_data()
        page = context["page_obj"]
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(
            page.number, on_each_side=3, on_ends=0
        )
        context["pagelist"] = pagelist
        return context


class BnADetail(DetailView):

    """BnaDetail Definition"""

    model = models.BnAPost
    context_object_name = "bna_detail"
    template_name = "posts/bna_detail.html"


class QnaView(ListView):

    """QnaView Definition"""

    model = models.QnaPost
    paginate_by = 10
    ordering = "-created"
    context_object_name = "qnas"
    template_name = "posts/qna.html"

    def get_context_data(self, **kwargs):
        context = super(QnaView, self).get_context_data()
        page = context["page_obj"]
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(
            page.number, on_each_side=3, on_ends=0
        )
        context["pagelist"] = pagelist
        return context


def QnaCheckView(request):
    if request.method == "POST":
        value = request.POST
        result = {}
        if value["i_seq"]:
            pk = value["i_seq"]
            password = value["secret_password"]
            qna = models.QnaPost.objects.get(pk=pk)
            if qna.password == password:
                result["check"] = "Success!"
                result["url"] = "/posts/qna/" + pk
            return HttpResponse(json.dumps(result), content_type="application/json")
        return HttpResponse(json.dumps(result), content_type="application/json")


class QnaDetail(DetailView):

    """QnaDetail Definition"""

    model = models.QnaPost
    context_object_name = "qna_detail"
    template_name = "posts/qna_detail.html"


class CreateQnaView(FormView):

    form_class = forms.CreateQnaForm
    template_name = "posts/qna_create.html"

    def form_valid(self, form):
        qna = form.save()
        qna.save()
        form.save_m2m()
        messages.success(self.request, "Qna Uploaded")
        return redirect(reverse("posts:qna_detail", kwargs={"pk": qna.pk}))


class CreateQnaAnswerView(FormView):

    form_class = forms.CreateQnaAnswerForm
    template_name = "posts/qna_detail.html"

    def form_valid(self, form):
        answer = form.save()
        answer.save()
        form.save_m2m()
        messages.success(self.request, "Qna Uploaded")
        return redirect(reverse("posts:qna_detail", kwargs={"pk": answer.pk}))


# @login_required()
def qna_a_delete(request, qna_pk):
    user = request.user
    print(user)
    # try:
    #     room = models.Room.objects.get(pk=qna_pk)
    #     if room.host.pk != user.pk:
    #         messages.error(request, "Can't delete that photo")
    #     else:
    #         models.Photo.objects.filter(pk=photo_pk).delete()
    #         messages.success(request, "Photo Deleted")
    #     return redirect(reverse("rooms:photos", kwargs={"pk": qna_pk}))
    # except models.Room.DoesNotExist:
    #     return redirect(reverse("core:home"))


class QnaAnswerEditView(UpdateView):

    model = models.QnaPost
    template_name = "posts/qna_edit.html"
    fields = ("name",)

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room


class NewsView(ListView):

    """NewsView Definition"""

    model = models.NewsPost
    paginate_by = 10
    ordering = "-created"
    context_object_name = "newses"
    template_name = "posts/news.html"

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data()
        page = context["page_obj"]
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(
            page.number, on_each_side=3, on_ends=0
        )
        context["pagelist"] = pagelist
        return context


class NewsDetail(DetailView):

    """NewsDetail Definition"""

    model = models.NewsPost
    context_object_name = "news_detail"
    template_name = "posts/news_detail.html"
