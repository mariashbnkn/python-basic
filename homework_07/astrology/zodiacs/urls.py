from django.urls import path

from .views import zodiacs_index, name_with_zodiacs_name

app_name = "zodiacs"

urlpatterns = [
    path("", zodiacs_index, name="index"),
    path("categories/", name_with_zodiacs_name, name="name_with_zodiacs_name"),
]
