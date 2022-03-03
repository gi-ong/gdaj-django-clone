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


class QnaPost(core_models.TimeStampedModel):

    """Post Model Definition"""

    TYPE_GNRAL = "gnral"
    TYPE_IMP = "imp"
    TYPE_ALIGN = "align"
    TYPE_BEAUTY = "beauty"

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
        "users.User", related_name="qna", on_delete=models.CASCADE, blank=True
    )
    # care_type = models.ForeignKey(
    #     "CareType", related_name="posts", on_delete=models.CASCADE, blank=True
    # )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:qna_detail", kwargs={"pk": self.pk})
