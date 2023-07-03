from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Zodiacs, ZodiacBase


def zodiacs_index(request: HttpRequest) -> HttpResponse:
    zodiacs = (
        Zodiacs
        .objects
        .filter(~Q(status=Zodiacs.Status.ARCHIVED))
        .order_by("id")
        .select_related("zodiac_name") # join
        # .defer(
        #     "description",
        #     "created_at",
        #     "updated_at",
        #     "category__description",
        # )
        .all()
    )

    return render(
        request=request,
        template_name="zodiacs/index.html",
        context={
            "zodiacs": zodiacs,
        },
    )


def name_with_zodiacs_name(request: HttpRequest) -> HttpResponse:
    zodiacs_base = ZodiacBase.objects.order_by("id").prefetch_related("zodiacs").all()

    return render(
        request=request,
        template_name="zodiacs/name_with_zodiacs_name.html",
        context={
            "zodiacs_base": zodiacs_base,
        }
    )
