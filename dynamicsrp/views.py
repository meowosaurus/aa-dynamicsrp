"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Subquery, OuterRef
from django.db.models import F
from django.db.models.functions import Coalesce
from django.core.cache import cache

from .models import *

def gen_context():
    all_settings = Setting.objects.all()

    context = {"display_all_ships": Setting.objects.get(name="display_all_ships"),
               "disable_ship_icons": Setting.objects.get(name="disable_ship_icons"),
               "disable_info_text": Setting.objects.get(name="disable_info_text"),
               "info_text": Setting.objects.get(name="info_text")}

    return context

@login_required
@permission_required("dynamicsrp.basic_access")
def payouts(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    ship_rows = Ship.objects.all().order_by("name")
    columns = Reimbursement.objects.all().order_by("index")
    column_width = 100 / (columns.count() + 1)

    context = gen_context()

    if not cache.get('matrix'):
        recalculate_matrix()

    matrix = cache.get('matrix')

    context.update({'header_rows': ship_rows, 
                'matrix': matrix,
                'columns': columns,
                'column_width': column_width})

    return render(request, "dynamicsrp/payouts.html", context)
