from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, ("Can't go there"))
        return redirect("pages:home")


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("users:login")


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {"message": "Successfully submitted form data."}
            return JsonResponse(data)
        else:
            return response
