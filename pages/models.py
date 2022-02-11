from django.db import models
from core import models as core_models
from posts.models import AbstractItem


class Branch(AbstractItem):

    """Branch Definition"""

    class Meta:
        verbose_name = "Branch"

    # class Page(core_models.TimeStampedModel):

    """Page Model Definition"""

    # BRANCH_ISU = "isu"
    # BRANCH_SNU = "snu"
    # BRANCH_GANGNAM = "gangnam"

    # BRANCH_CHOICES = (
    #     (BRANCH_ISU, "이수"),
    #     (BRANCH_SNU, "서울대입구"),
    #     (BRANCH_GANGNAM, "강남"),
    # )

    # branch = models.CharField(choices=BRANCH_CHOICES, max_length=10, blank=True)
