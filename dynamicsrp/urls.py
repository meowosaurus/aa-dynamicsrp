"""App URLs"""

# Django
from django.urls import path

# AA dynamicsrp App
from dynamicsrp import views

app_name: str = "dynamicsrp"

urlpatterns = [
    # User views

    path("", views.payouts, name="payouts"),
    path("requested/", views.requested, name="requested"),
    path("reports/", views.reports, name="reports"),

    # Admin views

    path("admin/open_requests/", views.open_requests, name="open_requests"),
    path("admin/closed_requests/", views.closed_requests, name="closed_requests"),
]
