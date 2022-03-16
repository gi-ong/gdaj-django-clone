from django.db import models
from core import models as core_models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# class CareType(AbstractItem):

#     """CareType Model Definition"""

#     class Meta:
#         verbose_name = "Care Type"


class BnAPhoto(core_models.TimeStampedModel):

    """BnAPhoto Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="bna_photos")
    bna = models.ForeignKey(
        "BnAPost", related_name="bna_photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class BnAPost(core_models.TimeStampedModel):

    """Post Model Definition"""

    TYPE_EVENT = "치아교정"
    TYPE_NOTICE = "치아미백"

    TYPE_CHOICES = (
        (TYPE_EVENT, "치아교정"),
        (TYPE_NOTICE, "치아미백"),
    )
    title = models.CharField(max_length=80)
    bna_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    # care_type = models.ForeignKey(
    #     "CareType", related_name="posts", on_delete=models.CASCADE, blank=True
    # )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:beforeafter_detail", kwargs={"pk": self.pk})

    def get_photos(self):
        try:
            photos = self.bna_photos.all()
            return photos
        except ValueError:
            return None


class NoticePhoto(core_models.TimeStampedModel):

    """NoticePhoto Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="n_photos")
    notice = models.ForeignKey(
        "NoticePost", related_name="notice_photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class NoticePost(core_models.TimeStampedModel):

    """Post Model Definition"""

    TYPE_EVENT = "이벤트"
    TYPE_NOTICE = "공지"

    TYPE_CHOICES = (
        (TYPE_EVENT, "event"),
        (TYPE_NOTICE, "notice"),
    )
    title = models.CharField(max_length=80)
    text = models.TextField()
    host = models.ForeignKey(
        "users.User", related_name="notice", on_delete=models.CASCADE
    )
    notice_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    # care_type = models.ForeignKey(
    #     "CareType", related_name="posts", on_delete=models.CASCADE, blank=True
    # )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:notice_detail", kwargs={"pk": self.pk})

    def get_photos(self):
        try:
            photos = self.notice_photos.all()
            return photos
        except ValueError:
            return None


class QnaAnswerPost(core_models.TimeStampedModel):

    """QnaAnswerPost Model Definition"""

    answer_text = models.TextField(blank=True)
    qnas = models.ForeignKey(
        "QnaPost", related_name="answers", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.answer_text

    def get_absolute_url(self):
        return reverse("posts:qna_detail", kwargs={"pk": self.qnas.pk})


class QnaPost(core_models.TimeStampedModel):

    """Post Model Definition"""

    TYPE_GNRAL = "일반치료"
    TYPE_IMP = "임플란트"
    TYPE_ALIGN = "치아교정"
    TYPE_BEAUTY = "치아미백"

    TYPE_CHOICES = (
        (TYPE_GNRAL, "일반치료"),
        (TYPE_IMP, "임플란트"),
        (TYPE_ALIGN, "치아교정"),
        (TYPE_BEAUTY, "치아미백"),
    )
    title = models.CharField(max_length=80)
    text = models.TextField()
    branch = models.ForeignKey(
        "pages.Branch", related_name="qna", on_delete=models.CASCADE
    )
    care_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(region="KR")
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=50)
    host = models.ForeignKey(
        "users.User",
        related_name="qna",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    answer_text = models.ForeignKey(
        "QnaAnswerPost",
        related_name="qna",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    # care_type = models.ForeignKey(
    #     "CareType", related_name="posts", on_delete=models.CASCADE, blank=True
    # )

    # def qna_answer(self):
    #     answer_text = self.answers.all()
    #     return answer_text

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:qna_detail", kwargs={"pk": self.pk})


class NewsPhoto(core_models.TimeStampedModel):

    """NewsPhoto Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="news_photo")
    notice = models.ForeignKey(
        "NewsPost", related_name="news_photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class NewsPost(core_models.TimeStampedModel):

    """Post Model Definition"""

    title = models.CharField(max_length=80)
    text = models.TextField()
    content = models.CharField(max_length=40)
    news_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:news_detail", kwargs={"pk": self.pk})

    def get_photos(self):
        try:
            photos = self.news_photos.all()
            return photos
        except ValueError:
            return None
