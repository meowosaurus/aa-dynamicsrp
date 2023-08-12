"""App URLs"""

# Django
from django.urls import path

# AA dynamicsrp App
from dynamicsrp import views

app_name: str = "dynamicsrp"

urlpatterns = [
    path("", views.index, name="index"),
]
