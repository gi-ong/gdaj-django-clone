from django.db import models
from core import models as core_models
from posts.models import AbstractItem
from django.urls import reverse


class Branch(AbstractItem):

    """Branch Definition"""

    class Meta:
        verbose_name = "Branch"


class BranchWithUrl(core_models.TimeStampedModel):

    branch_name = models.ForeignKey(
        "Branch", related_name="branches", on_delete=models.CASCADE
    )
    url_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse("pages:branch")
