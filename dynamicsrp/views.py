"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Subquery, OuterRef
from django.db.models import F
from django.db.models.functions import Coalesce
from django.core.cache import cache

from .models import *

# Utilities

def gen_context():
    all_settings = Setting.objects.all()

    # Recalculate data if not available in memory
    if not cache.get('matrix'):
        recalculate_matrix()
    if not cache.get('settings'):
        load_settings()

    context = {"display_all_ships": Setting.objects.get(name="display_all_ships"),
               "disable_ship_icons": Setting.objects.get(name="disable_ship_icons"),
               "disable_info_text": Setting.objects.get(name="disable_info_text"),
               "info_text": Setting.objects.get(name="info_text"),
               "settings": cache.get("settings")}

    return context

# User views

@login_required
@permission_required("dynamicsrp.payouts_access")
def payouts(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    context = gen_context()

    ship_rows = Ship.objects.all().order_by("name")
    columns = Reimbursement.objects.all().order_by("index")
    column_width = 100 / (columns.count() + 1)

    matrix = cache.get('matrix')

    context.update({'header_rows': ship_rows, 
                'matrix': matrix,
                'columns': columns,
                'column_width': column_width})

    return render(request, "dynamicsrp/payouts.html", context)

@login_required
@permission_required("dynamicsrp.requests_access")
def requested(request: WSGIRequest) -> HttpResponse:

    context = gen_context()

    settings = cache.get('settings')
    if settings['disable_request_functionality'] == "False":

        all_requests = SRPRequest.objects.all()

        context.update({'requests': all_requests})

        return render(request, "dynamicsrp/requested.html", context)

    else:

        return redirect('dynamicsrp:payouts')


@login_required
@permission_required("dynamicsrp.reports_access")
def reports(request: WSGIRequest) -> HttpResponse:

    settings = cache.get('settings')
    if settings['disable_request_functionality'] == "False":
        context = gen_context()

        return render(request, "dynamicsrp/reports.html", context)
    else:
        return redirect('dynamicsrp:payouts')

# Admin views

@login_required
@permission_required("dynamicsrp.basic_access")
def open_requests(request: WSGIRequest) -> HttpResponse:

    settings = cache.get('settings')
    if settings['disable_request_functionality'] == "False":
        context = gen_context()

        return render(request, "dynamicsrp/admin/open_requests.html", context)
    else:
        return redirect('dynamicsrp:payouts')

@login_required
@permission_required("dynamicsrp.basic_access")
def closed_requests(request: WSGIRequest) -> HttpResponse:

    settings = cache.get('settings')
    if settings['disable_request_functionality'] == "False":
        context = gen_context()

        return render(request, "dynamicsrp/admin/closed_requests.html", context)
    else:
        return redirect('dynamicsrp:payouts')
