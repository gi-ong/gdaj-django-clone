from django.db import models
from core import models as core_models
from phonenumber_field.modelfields import PhoneNumberField


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


class Post(core_models.TimeStampedModel):

    # """Post Model Definition"""
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
    branch = models.ForeignKey(
        "pages.Branch", related_name="posts", on_delete=models.CASCADE
    )
    care_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(region="KR")
    text = models.TextField()
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=50)

    # care_type = models.ForeignKey(
    #     "CareType", related_name="posts", on_delete=models.CASCADE, blank=True
    # )
