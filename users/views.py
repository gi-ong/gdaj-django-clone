from multiprocessing import AuthenticationError
from django.shortcuts import render, reverse, redirect, resolve_url
from django.views.generic import FormView
from . import mixins, forms, models
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
import json


def ajax_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        response_data = {}
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                form = forms.LoginForm()
                login(request, user)
                response_data["result"] = "Success!"
                response_data["message"] = 'You"re logged in'
            else:
                response_data["errors"] = "failed"
                response_data["captcha"] = "good"
                response_data["message"] = "You messed up"
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    # username = request.GET.get("username")
    # password = request.GET.get("password")
    # user = authenticate(username=username, password=password)
    # response_data = {}
    # if user.is_active:
    #     response_data["result"] = "Success!"
    #     response_data["message"] = 'You"re logged in'
    # else:
    #     response_data["errors"] = True
    #     response_data["captcha"] = True
    #     response_data["message"] = "You messed up"

    # return HttpResponse(json.dumps(response_data), content_type="application/json")


class LoginView(mixins.LoggedOutOnlyView, FormView):
    form_class = forms.LoginForm
    # template_name = "users/login.html"
    template_name = "main.html"
    success_url = "/user/ajaxlogin/"

    def form_invalid(self, form):
        response = super(LoginView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(
                data={"result": False, "errors": form.errors}, safe=True, status=400
            )
        else:
            return response

    def form_valid(self, form):
        response = super(LoginView, self).form_valid(form)
        if self.request.is_ajax():
            print(response)
            # data = {"message": "Successfully submitted form data."}
            return JsonResponse(data={"result": True}, safe=True, status=200)
        else:
            return response


# class LoginView(mixins.AjaxFormMixin, FormView):
#     form_class = forms.LoginForm
#     # template_name = "users/login.html"
#     template_name = "main.html"
#     success_url = "/user/ajaxlogin/"

#     def form_invalid(self, form):
#         response = super(LoginView, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response

#     def form_valid(self, form):
#         response = super(LoginView, self).form_valid(form)
#         if self.request.is_ajax():
#             print(response)
#             data = {"message": "Successfully submitted form data."}
#             return JsonResponse(data)
#         else:
#             return response


# class LoginView(FormView):
#     template_name = "users/login.html"
#     form_class = forms.LoginForm

#     def form_valid(self, form):
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)

#     def get_success_url(self):
#         next_arg = self.request.GET.get("next")
#         if next_arg is not None:
#             return next_arg
#         else:
#             return reverse("pages:home")


def log_out(request):
    messages.info(request, f"See you later {request.user.first_name}")
    logout(request)
    return redirect(reverse("pages:home"))


class SignUpView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get("next") or "/"
        return resolve_url(next_url)


# mixins.LoggedOutOnlyView,
