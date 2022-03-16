from django.views.generic import ListView
from . import models


class BranchView(ListView):
    """BranchView Definition"""

    model = models.BranchWithUrl
    context_object_name = "branches"
    template_name = "intro/intro_branch.html"
