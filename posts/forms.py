from django import forms
from . import models


class CreateQnaForm(forms.ModelForm):
    class Meta:
        model = models.QnaPost
        fields = (
            "title",
            "text",
            "branch",
            "care_type",
            "name",
            "phone",
            "email",
            "password",
            "host",
        )

    def __init__(self, *args, **kwargs):
        super(CreateQnaForm, self).__init__(*args, **kwargs)
        self.fields["branch"].widget.attrs = {
            "class": "counsel_select_left",
            "id": "id_branch",
        }
        self.fields["care_type"].widget.attrs = {
            "id": "id_qna_type",
        }
        self.fields["title"].widget.attrs = {
            "id": "id_title",
            "placeholder": "제목을 입력해주세요.",
            "maxlength": "150",
        }
        self.fields["name"].widget.attrs = {
            "id": "id_author",
            "placeholder": "이름을 입력해주세요.",
            "maxlength": "90",
            "class": "counsel_input_left",
        }
        self.fields["password"].widget.attrs = {
            "type": "password",
            "id": "id_qna_passwd",
            "placeholder": "비밀번호를 입력해주세요.",
            "maxlength": "255",
        }
        self.fields["phone"].widget.attrs = {
            "id": "id_phone_number",
            "placeholder": "연락처를 입력해주세요.",
            "maxlength": "11",
            "class": "counsel_input_left only_number",
        }
        self.fields["email"].widget.attrs = {
            "id": "id_email",
            "placeholder": "이메일을 입력해주세요.",
            "maxlength": "254",
        }
        self.fields["text"].widget.attrs = {
            "id": "id_contents",
            "placeholder": "내용을 입력해주세요.",
            "cols": "40",
            "rows": "10",
        }

    def save(self, *args, **kwargs):
        qna = super().save(commit=False)
        return qna


class CreateQnaAnswerForm(forms.ModelForm):
    class Meta:
        model = models.QnaPost
        fields = ("answer_text",)

    def __init__(self, *args, **kwargs):
        super(CreateQnaAnswerForm, self).__init__(*args, **kwargs)
        self.fields["answer_text"].widget.attrs = {
            "id": "id_answers",
            "placeholder": "내용을 입력해주세요.",
            "cols": "40",
            "rows": "10",
        }

    def save(self, *args, **kwargs):
        answer = super().save(commit=False)
        return answer


#     def clean(self):
#         password = self.cleaned_data.get("password")
#         try:
#             user = models.QnaPost.objects.get(username=username)
#             if user.check_password(password):
#                 return self.cleaned_data
#             else:
#                 self.add_error("password", forms.ValidationError("Password is wrong"))
#         except models.User.DoesNotExist:
#             self.add_error("username", forms.ValidationError("User does not exist"))
